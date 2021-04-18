# Django Vaccine Dashboard

Django project to demonstrate how to implement a Covid-19 vaccination dashboard with Django and Chart.js.

Check out my [blog post](https://www.samuelliedtke.com/blog/build-covid-19-vaccination-dashboard-django-and-chartjs-part-1/) where I go through building it from the ground up step by step.

The project is not completed yet and will be updated with once I've published the follow-up blog post.

## 🙌 Thanks
Thanks to @gabrielpreda for providing and constantly updating the dataset on [Kaggle](https://www.kaggle.com/gpreda/covid-world-vaccination-progress).

## 📖 Installation
```shell
$ python3 -m venv venv
$ source venv/bin/activate    (on Mac)
$ venv/Source/activate        (on Windows)
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt
(venv) $ python manage.py migrate
(venv) $ python manage.py createsuperuser
(venv) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

## 🤝 Contributing
Contributions, issues and feature requests are welcome! 

## ⭐️ Support
Give a ⭐️ if this project helped you!

## License
[The MIT License](https://github.com/jimmybutton/django-blogcomments/blob/master/LICENSE)