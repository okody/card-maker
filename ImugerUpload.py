from StuffCards.Auth import authenticate
from datetime import datetime

album = None
image_path = 'StaffCards/JackoffFounder.png'

def upload_image(client):
    config = {
        'album': album,
        'name': 'Something',
        'title': 'Founder',
        'description': 'None'
    }
    print('Uploading....')
    image = client.upload_from_path(image_path,config=config,anon=False)
    print('Done')
    return image

if __name__ == '__main__':
    client = authenticate()
    image = upload_image(client)
    upload_image(client)
    print('image posed')
    print('YOu can get that here: {}'.format(image['link']))