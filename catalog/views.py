from django.shortcuts import render
from django.http import Http404
from .data import (
    get_all_categories, get_category_by_id, get_all_services, 
    get_service_by_id, get_services_by_category, search_services,
    get_category_name, get_dashboard_stats
)


def service_catalog_list(request):
    """View untuk menampilkan daftar semua layanan"""
    query = request.GET.get('search', '').strip()
    category_id = request.GET.get('category', '')
    
    # Get all services and categories
    services = get_all_services()
    categories = get_all_categories()
    
    # Add service count to each category
    for category in categories:
        category['service_count'] = len(get_services_by_category(category['id']))
    
    # Apply search filter
    if query:
        services = search_services(query)
    
    # Apply category filter
    if category_id:
        try:
            category_id = int(category_id)
            services = get_services_by_category(category_id)
            if query:  # If both search and category filter
                services = [s for s in services if query.lower() in s['name'].lower() or query.lower() in s['description'].lower()]
        except (ValueError, TypeError):
            pass
    
    # Add category name to each service
    for service in services:
        service['category_name'] = get_category_name(service['category_id'])
    
    # Get selected category name for display
    selected_category_name = None
    if category_id:
        selected_category_name = get_category_name(category_id)
    
    context = {
        'categories': categories,
        'services': services,
        'selected_category': category_id if category_id else None,
        'selected_category_name': selected_category_name,
        'search_query': query,
    }
    return render(request, 'catalog/service_list.html', context)


def service_detail(request, service_id):
    """View untuk menampilkan detail layanan"""
    service = get_service_by_id(service_id)
    if not service:
        raise Http404("Service not found")
    
    # Add category information
    service['category_name'] = get_category_name(service['category_id'])
    
    # Get related services from the same category
    related_services = get_services_by_category(service['category_id'])
    related_services = [s for s in related_services if s['id'] != service['id']][:3]
    
    context = {
        'service': service,
        'related_services': related_services,
    }
    return render(request, 'catalog/service_detail.html', context)


def category_detail(request, category_id):
    """View untuk menampilkan layanan berdasarkan kategori"""
    category = get_category_by_id(category_id)
    if not category:
        raise Http404("Category not found")
    
    services = get_services_by_category(category_id)
    all_categories = get_all_categories()
    
    # Add service count to each category
    for cat in all_categories:
        cat['service_count'] = len(get_services_by_category(cat['id']))
    
    # Add category name to each service
    for service in services:
        service['category_name'] = category['name']
    
    # Calculate unique PICs for this category
    unique_pics = set(service['pic'] for service in services)
    unique_pic_count = len(unique_pics)
    
    context = {
        'category': category,
        'services': services,
        'all_categories': all_categories,
        'unique_pic_count': unique_pic_count,
    }
    return render(request, 'catalog/category_detail.html', context)


def dashboard(request):
    """Dashboard view dengan statistik layanan"""
    stats = get_dashboard_stats()
    categories = get_all_categories()
    
    # Add service count to each category for services_by_category
    services_by_category = []
    for category in categories:
        service_count = len(get_services_by_category(category['id']))
        services_by_category.append({
            'id': category['id'],
            'name': category['name'],
            'description': category['description'],
            'service_count': service_count
        })
    
    # Sort by service count descending
    services_by_category.sort(key=lambda x: x['service_count'], reverse=True)
    
    # Get recent services (last 5)
    recent_services = get_all_services()[-5:]
    for service in recent_services:
        service['category_name'] = get_category_name(service['category_id'])
    
    # PIC statistics
    pic_count = {}
    for service in get_all_services():
        pic = service['pic']
        pic_count[pic] = pic_count.get(pic, 0) + 1
    
    pic_stats = [{'pic': pic, 'count': count} for pic, count in pic_count.items()]
    pic_stats.sort(key=lambda x: x['count'], reverse=True)
    pic_stats = pic_stats[:5]  # Top 5
    
    context = {
        'total_services': stats['total_services'],
        'total_categories': stats['total_categories'],
        'services_by_category': services_by_category,
        'recent_services': recent_services,
        'pic_stats': pic_stats,
    }
    return render(request, 'catalog/dashboard.html', context)
