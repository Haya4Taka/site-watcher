import sys
sys.path.append('/Users/takahiro/projects/site-watcher/')
from src.usecases.interactor.property_usecase_impl import PropertyUsecaseImpl
from src.usecases.interactor.user_usecase_impl import UserUseaseImpl
from src.repository.property_repository_impl import PropertyRepositoryImpl
from src.repository.user_repository_impl import UserRepositoryImpl
from src.domain.model.user import User
from dataclasses import asdict
import json

users = UserUseaseImpl(UserRepositoryImpl()).get_all()

for user in users:
    user
url = "http://www.guesthousebank.com/a_detail/q_13626/"

src = PropertyUsecaseImpl(PropertyRepositoryImpl()).find(url)
res = json.dumps(asdict(src), ensure_ascii=False, indent=0)
path = "/Users/takahiro/projects/site-watcher/test.text"
with open(path, mode='w') as f:
    f.write(res)
