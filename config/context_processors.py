def active_nav_context(request):
    return {
        'is_blog_active': request.path.startswith('/blog'),
        'is_forum_active': request.path.startswith('/forum'),
        'is_chat_active': request.path.startswith('/chat'),
        'is_booking_active': request.path.startswith('/booking'),
        'is_social_active': request.path.startswith('/social'),
    }