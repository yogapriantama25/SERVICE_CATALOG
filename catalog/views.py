from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from .models import Category, Service


def service_catalog_list(request):
    """View untuk menampilkan daftar semua layanan"""
    categories = Category.objects.prefetch_related('services').all()
    services = Service.objects.filter(is_active=True).select_related('category')
    
    # Filter berdasarkan kategori jika ada
    category_filter = request.GET.get('category')
    if category_filter:
        services = services.filter(category__id=category_filter)
    
    # Search functionality
    search_query = request.GET.get('search', '').strip()
    if search_query:
        services = services.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(users__icontains=search_query) |
            Q(request_method__icontains=search_query) |
            Q(pic__icontains=search_query)
        )
    
    context = {
        'categories': categories,
        'services': services,
        'selected_category': category_filter,
        'search_query': search_query,
    }
    return render(request, 'catalog/service_list.html', context)


def service_detail(request, service_id):
    """View untuk menampilkan detail layanan"""
    service = get_object_or_404(Service, id=service_id, is_active=True)
    context = {
        'service': service,
    }
    return render(request, 'catalog/service_detail.html', context)


def category_detail(request, category_id):
    """View untuk menampilkan layanan berdasarkan kategori"""
    category = get_object_or_404(Category, id=category_id)
    services = Service.objects.filter(category=category, is_active=True)
    all_categories = Category.objects.all()
    
    context = {
        'category': category,
        'services': services,
        'all_categories': all_categories,
    }
    return render(request, 'catalog/category_detail.html', context)


def dashboard(request):
    """Dashboard view dengan statistik layanan"""
    # Statistics
    total_services = Service.objects.filter(is_active=True).count()
    total_categories = Category.objects.count()
    
    # Services by category
    services_by_category = Category.objects.annotate(
        service_count=Count('services', filter=Q(services__is_active=True))
    ).order_by('-service_count')
    
    # Recent services (last 5 updated)
    recent_services = Service.objects.filter(is_active=True).order_by('-updated_at')[:5]
    
    # PIC statistics
    pic_stats = Service.objects.filter(is_active=True).values('pic').annotate(
        count=Count('id')
    ).order_by('-count')[:5]
    
    context = {
        'total_services': total_services,
        'total_categories': total_categories,
        'services_by_category': services_by_category,
        'recent_services': recent_services,
        'pic_stats': pic_stats,
    }
    return render(request, 'catalog/dashboard.html', context)
