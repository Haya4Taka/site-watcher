from dataclasses import asdict
from flask import Blueprint, request
property_module = Blueprint('property', __name__)
from src.usecases.interactor.property_usecase_impl import PropertyUsecaseImpl
from src.repository.property_repository_impl import PropertyRepositoryImpl
# from flask import Blueprint, request
# property_module = Blueprint('property', __name__)
import json

# property_module = Blueprint('property', __name__)

@property_module.route('/property')
def property():
    url = request.args.get('url')
    rsc = PropertyUsecaseImpl(PropertyRepositoryImpl()).find(url)
    res = json.dumps(asdict(rsc), ensure_ascii=False, indent=0)
    return res
