from django.shortcuts import render


def home(request):
    packages = [
	{'name':'blasy', 'url': 'http://pypi.python.org/pypi/blasy/0.1.2'},
	{'name':'BlastRadius', 'url': 'http://pypi.python.org/pypi/BlastRadius/0.1.6'},
	{'name':'chainercmd', 'url': 'http://pypi.python.org/pypi/chainercmd/3.1.0a2'},
	{'name':'chainer-chemistry', 'url': 'http://pypi.python.org/pypi/chainer-chemistry/0.1.0'},
	{'name':'chainerboard', 'url': 'http://pypi.python.org/pypi/chainerboard/0.1.5'},
	{'name':'django-allauth', 'url': 'https://pypi.org/project/django-allauth/0.38.0/'},
	{'name':'django-bootstrap4', 'url': 'https://pypi.org/project/django-bootstrap4/0.0.7/'},
	{'name':'djangorestframework', 'url': 'https://pypi.org/project/djangorestframework/3.9.0/'},
    ]
    context = {
        'packages': packages
    }
    return render(request, 'home/index.html', context)
