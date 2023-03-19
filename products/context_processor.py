from .models import MainImage

def render_header(request):
    ''' Returns necessary information for footer rendering
    '''
    main_image = MainImage.objects.all()[:2]
    
    return {
        'main_image':main_image
    }