# Static data for the service catalog - no database required
from datetime import datetime, timedelta
from django.utils import timezone

# Generate some realistic dates
now = timezone.now()
base_date = now - timedelta(days=30)

CATEGORIES = [
    {
        'id': 1,
        'name': 'Infrastructure Services',
        'description': 'Core infrastructure and platform services for development and operations',
        'icon': 'fas fa-server'
    },
    {
        'id': 2,
        'name': 'Development Tools',
        'description': 'Tools and services for software development and version control',
        'icon': 'fas fa-code'
    },
    {
        'id': 3,
        'name': 'Security Services',
        'description': 'Security, compliance, and access management services',
        'icon': 'fas fa-shield-alt'
    },
    {
        'id': 4,
        'name': 'Monitoring & Analytics',
        'description': 'Monitoring, logging, and analytics platforms',
        'icon': 'fas fa-chart-bar'
    },
    {
        'id': 5,
        'name': 'Communication & Collaboration',
        'description': 'Communication tools and collaboration platforms',
        'icon': 'fas fa-comments'
    }
]

SERVICES = [
    # Infrastructure Services
    {
        'id': 1,
        'name': 'AWS EC2 Instance',
        'description': 'Virtual machine instances for computing needs with flexible sizing options',
        'category_id': 1,
        'users': 150,
        'request_method': 'Self-Service Portal',
        'sla': '2 hours',
        'pic': 'Infrastructure Team',
        'icon': 'fab fa-aws',
        'created_at': base_date,
        'updated_at': now - timedelta(days=2)
    },
    {
        'id': 2,
        'name': 'Kubernetes Cluster',
        'description': 'Managed Kubernetes clusters for container orchestration and microservices',
        'category_id': 1,
        'users': 85,
        'request_method': 'Service Desk Ticket',
        'sla': '4 hours',
        'pic': 'DevOps Team',
        'icon': 'fas fa-cubes'
    },
    {
        'id': 3,
        'name': 'Load Balancer',
        'description': 'Application load balancers for high availability and traffic distribution',
        'category_id': 1,
        'users': 120,
        'request_method': 'Self-Service Portal',
        'sla': '1 hour',
        'pic': 'Network Team',
        'icon': 'fas fa-balance-scale'
    },
    
    # Development Tools
    {
        'id': 4,
        'name': 'GitLab Repository',
        'description': 'Git repositories with CI/CD pipelines and project management features',
        'category_id': 2,
        'users': 200,
        'request_method': 'Self-Service Portal',
        'sla': '30 minutes',
        'pic': 'Development Team',
        'icon': 'fab fa-gitlab'
    },
    {
        'id': 5,
        'name': 'Jenkins Build Server',
        'description': 'Automated build and deployment pipelines for continuous integration',
        'category_id': 2,
        'users': 75,
        'request_method': 'Service Desk Ticket',
        'sla': '2 hours',
        'pic': 'DevOps Team',
        'icon': 'fas fa-hammer'
    },
    {
        'id': 6,
        'name': 'SonarQube Code Quality',
        'description': 'Code quality analysis and security vulnerability scanning',
        'category_id': 2,
        'users': 90,
        'request_method': 'Self-Service Portal',
        'sla': '1 hour',
        'pic': 'Quality Assurance Team',
        'icon': 'fas fa-search'
    },
    
    # Security Services
    {
        'id': 7,
        'name': 'VPN Access',
        'description': 'Secure remote access to internal networks and resources',
        'category_id': 3,
        'users': 250,
        'request_method': 'Service Desk Ticket',
        'sla': '24 hours',
        'pic': 'Security Team',
        'icon': 'fas fa-lock'
    },
    {
        'id': 8,
        'name': 'SSL Certificate',
        'description': 'SSL/TLS certificates for secure web communications',
        'category_id': 3,
        'users': 180,
        'request_method': 'Service Desk Ticket',
        'sla': '48 hours',
        'pic': 'Security Team',
        'icon': 'fas fa-certificate'
    },
    {
        'id': 9,
        'name': 'Identity Management',
        'description': 'User identity and access management with single sign-on',
        'category_id': 3,
        'users': 300,
        'request_method': 'HR Approval Required',
        'sla': '4 hours',
        'pic': 'Identity Team',
        'icon': 'fas fa-user-shield'
    },
    
    # Monitoring & Analytics
    {
        'id': 10,
        'name': 'Prometheus Monitoring',
        'description': 'System and application monitoring with alerting capabilities',
        'category_id': 4,
        'users': 95,
        'request_method': 'Self-Service Portal',
        'sla': '2 hours',
        'pic': 'Operations Team',
        'icon': 'fas fa-eye'
    },
    {
        'id': 11,
        'name': 'ELK Stack Logging',
        'description': 'Centralized logging and log analysis with Elasticsearch, Logstash, and Kibana',
        'category_id': 4,
        'users': 110,
        'request_method': 'Service Desk Ticket',
        'sla': '3 hours',
        'pic': 'Operations Team',
        'icon': 'fas fa-file-alt'
    },
    {
        'id': 12,
        'name': 'Grafana Dashboard',
        'description': 'Customizable dashboards for metrics visualization and analysis',
        'category_id': 4,
        'users': 130,
        'request_method': 'Self-Service Portal',
        'sla': '1 hour',
        'pic': 'Operations Team',
        'icon': 'fas fa-tachometer-alt'
    },
    
    # Communication & Collaboration
    {
        'id': 13,
        'name': 'Microsoft Teams',
        'description': 'Team communication, video conferencing, and file sharing platform',
        'category_id': 5,
        'users': 400,
        'request_method': 'HR Approval Required',
        'sla': '2 hours',
        'pic': 'IT Support Team',
        'icon': 'fab fa-microsoft'
    },
    {
        'id': 14,
        'name': 'Confluence Wiki',
        'description': 'Team collaboration space for documentation and knowledge sharing',
        'category_id': 5,
        'users': 220,
        'request_method': 'Self-Service Portal',
        'sla': '1 hour',
        'pic': 'Documentation Team',
        'icon': 'fab fa-confluence'
    },
    {
        'id': 15,
        'name': 'Jira Project Management',
        'description': 'Project tracking, issue management, and agile development workflows',
        'category_id': 5,
        'users': 180,
        'request_method': 'Project Manager Approval',
        'sla': '4 hours',
        'pic': 'Project Management Office',
        'icon': 'fab fa-jira'
    }
]

def get_all_categories():
    """Get all categories"""
    return CATEGORIES

def get_category_by_id(category_id):
    """Get a specific category by ID"""
    try:
        category_id = int(category_id)
        for category in CATEGORIES:
            if category['id'] == category_id:
                return category
    except (ValueError, TypeError):
        pass
    return None

def get_all_services():
    """Get all services"""
    return SERVICES

def get_service_by_id(service_id):
    """Get a specific service by ID"""
    try:
        service_id = int(service_id)
        for service in SERVICES:
            if service['id'] == service_id:
                return service
    except (ValueError, TypeError):
        pass
    return None

def get_services_by_category(category_id):
    """Get all services for a specific category"""
    try:
        category_id = int(category_id)
        return [service for service in SERVICES if service['category_id'] == category_id]
    except (ValueError, TypeError):
        return []

def search_services(query):
    """Search services by name or description"""
    if not query:
        return SERVICES
    
    query = query.lower()
    results = []
    
    for service in SERVICES:
        if (query in service['name'].lower() or 
            query in service['description'].lower() or
            query in service['pic'].lower()):
            results.append(service)
    
    return results

def get_category_name(category_id):
    """Get category name by ID"""
    category = get_category_by_id(category_id)
    return category['name'] if category else 'Unknown Category'

def get_dashboard_stats():
    """Get dashboard statistics"""
    total_services = len(SERVICES)
    total_categories = len(CATEGORIES)
    total_users = sum(service['users'] for service in SERVICES)
    
    # Calculate average SLA
    sla_hours = []
    for service in SERVICES:
        sla = service['sla']
        if 'hour' in sla:
            hours = int(sla.split()[0])
            sla_hours.append(hours)
        elif 'minute' in sla:
            minutes = int(sla.split()[0])
            sla_hours.append(minutes / 60)
    
    avg_sla = sum(sla_hours) / len(sla_hours) if sla_hours else 0
    
    return {
        'total_services': total_services,
        'total_categories': total_categories,
        'total_users': total_users,
        'avg_sla_hours': round(avg_sla, 1)
    }