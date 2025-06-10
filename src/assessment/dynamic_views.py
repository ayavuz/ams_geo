from rest_framework.routers import DefaultRouter
from django.db import models
import json
import os
from django.conf import settings


def create_dynamic_model(object_config):
    """
        dynamisch model aanmaken
    """
    
    field_mapping = {
        'string': models.CharField(max_length=255),
        'boolean': models.BooleanField(default=False),
        'datetime': models.DateTimeField(),
    }
    
    model_fields = {
        'id': models.AutoField(primary_key=True),
        '__module__': 'dynamic_models',
    }
    
    for field_config in object_config['fields']:
        field_name = field_config['name']
        field_type = field_config['type']
        
        field = field_mapping.get(field_type, models.CharField(max_length=255))
        field.null = True
        field.blank = True
            
        model_fields[field_name] = field
    
    model_class = type(
        object_config['name'].capitalize(),
        (models.Model,),
        model_fields
    )
    
    return model_class


def init_dynamic_api(config_file):
    """
        setup van dynamic apis
    """

    if not os.path.isabs(config_file):
        config_path = os.path.join(settings.BASE_DIR, config_file)
    else:
        config_path = config_file
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    router = DefaultRouter()
    
    for object_config in config['objects']:

        print('x'*50)
        print(object_config)
        print('x'*50)
        

        # TODO create dynamic model
        # create_dynamic_model(object_config)

        # TODO create dynamic viewset

        # TODO create dynamic endpoint

        pass
    
    return router