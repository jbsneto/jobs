import requests, datetime


def _url():
    return "https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume"

def _data():
    return {
        "full_name": "Jose Bernardino dos Santos Neto",
        "email": "josebernardinoneto@gmail.com",
        "mobile_phone": "+55 (83) 999505284",
        "age": 26,
        "home_address": "37 Rua Panatis, Belo Horizonte, Patos, Paraiba",
        "start_date": int(datetime.datetime.now().timestamp()),
        "opportunity_tag": "dev_intern_200",
        "past_jobs_experience": "99 taxi - freelance - python/django; EasyWeb - 4 months - python/django; Patos24Horas - one year - python/django; Linkedin: https://www.linkedin.com/in/jose-bernardino-neto-98407b66/ ",
        "degrees": [{
            "institution_name": "UNIFIP - Centro Universitario de Patos",
            "degree_name": "Information Systems",
            "begin_date": int(datetime.datetime(2013,2,1,0,0).timestamp()),
            "end_date": int(datetime.datetime(2017,12,1,0,0).timestamp())
        }],
        "programming_skills": ["python/django", "django rest framework"],
        "database_skills": ["mysql", "postgresql", "sqlite"],
        "hobbies": ["rock climb", "trekking"],
        "why": "I am a junior developer and new father, looking for a opportunity to change life. Working in the dream job and giving a plus in the financial life.",
        "git_url_repositories": "https://github.com/jbsneto"
    }

def post_profile(url, data):
    try:
        response = requests.post(url=url, data=data)
    except requests.exceptions.RequestException as e:
        return e
    finally:
        return response


if __name__ == '__main__':
    url = _url()
    data = _data()

    print(post_profile(url, data))
