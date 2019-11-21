%define srcname django-hosts
%define version 3.1.dev6+g316c340
%define release 3

Summary: Dynamic and static host resolving for Django. Maps hostnames to URLconfs.
Name: python-%{srcname}
Version: %{version}
Release: %{release}
Source0: %{srcname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildArch: noarch
Vendor: Jannis Leidel <jannis@leidel.info>
BuildRequires: python2-devel python3-devel

%description
This Django app routes requests for specific hosts to different URL schemes
defined in modules called "hostconfs".

For example, if you own ``example.com`` but want to serve specific content
at ``api.example.com`` and ``beta.example.com``, add the following to a
``hosts.py`` file::

    from django_hosts import patterns, host

    host_patterns = patterns('path.to',
        host(r'api', 'api.urls', name='api'),
        host(r'beta', 'beta.urls', name='beta'),
    )

This causes requests to ``{api,beta}.example.com`` to be routed to their
corresponding URLconf. You can use your ``urls.py`` as a template for these
hostconfs.

Patterns are evaluated in order. If no pattern matches, the request is
processed in the usual way, ie. using the standard ``ROOT_URLCONF``.

The patterns on the left-hand side are regular expressions. For example,
the following ``ROOT_HOSTCONF`` setting will route ``foo.example.com``
and ``bar.example.com`` to the same URLconf.


    from django_hosts import patterns, host

    host_patterns = patterns('',
        host(r'(foo|bar)', 'path.to.urls', name='foo-or-bar'),
    )

 note:

  Remember:

  * Patterns are matched against the extreme left of the requested host

  * It is implied that all patterns end either with a literal full stop
    (ie. ".") or an end of line metacharacter.

  * As with all regular expressions, various metacharacters need quoting.


 repository on Github: https://github.com/jazzband/django-hosts
 django-hosts.rtfd.org: https://django-hosts.readthedocs.io/


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}

This Django app routes requests for specific hosts to different URL schemes
defined in modules called "hostconfs".

For example, if you own ``example.com`` but want to serve specific content
at ``api.example.com`` and ``beta.example.com``, add the following to a
``hosts.py`` file::

    from django_hosts import patterns, host

    host_patterns = patterns('path.to',
        host(r'api', 'api.urls', name='api'),
        host(r'beta', 'beta.urls', name='beta'),
    )

This causes requests to ``{api,beta}.example.com`` to be routed to their
corresponding URLconf. You can use your ``urls.py`` as a template for these
hostconfs.

Patterns are evaluated in order. If no pattern matches, the request is
processed in the usual way, ie. using the standard ``ROOT_URLCONF``.

The patterns on the left-hand side are regular expressions. For example,
the following ``ROOT_HOSTCONF`` setting will route ``foo.example.com``
and ``bar.example.com`` to the same URLconf.

::

    from django_hosts import patterns, host

    host_patterns = patterns('',
        host(r'(foo|bar)', 'path.to.urls', name='foo-or-bar'),
    )

.. note:

  Remember:

  * Patterns are matched against the extreme left of the requested host

  * It is implied that all patterns end either with a literal full stop
    (ie. ".") or an end of line metacharacter.

  * As with all regular expressions, various metacharacters need quoting.

Installation
------------

First, install the app with your favorite package manager, e.g.::

    pip install django-hosts

Alternatively, use the `repository on Github`_.

You can find the full docs here: `django-hosts.rtfd.org`_

Then configure your Django site to use the app:

#. Add ``'django_hosts'`` to your ``INSTALLED_APPS`` setting.

#. Add ``'django_hosts.middleware.HostsRequestMiddleware'`` to the **beginning** of your
   ``MIDDLEWARE`` or ``MIDDLEWARE_CLASSES`` setting.

#. Add ``'django_hosts.middleware.HostsResponseMiddleware'`` to the **end** of your
   ``MIDDLEWARE`` or ``MIDDLEWARE_CLASSES`` setting.

#. Create a new module containing your default host patterns,
   e.g. in the ``hosts.py`` file next to your ``urls.py``.

#. Set the ``ROOT_HOSTCONF`` setting to the dotted Python
   import path of the module containing your host patterns, e.g.::

       ROOT_HOSTCONF = 'mysite.hosts'
  
#. Set the ``DEFAULT_HOST`` setting to the **name** of the host pattern you
   want to refer to as the default pattern. It'll be used if no other
   pattern matches or you don't give a name to the ``host_url`` template
   tag.

.. _`repository on Github`: https://github.com/jazzband/django-hosts
.. _`django-hosts.rtfd.org`: https://django-hosts.readthedocs.io/


%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

#%check
#%{__python2} setup.py test
#%{__python3} setup.py test


%files -n %{name}
#%license LICENSE
%doc README.rst
%{python2_sitelib}/*

%files -n python3-%{srcname}
#%license LICENSE
%doc README.rst
%{python3_sitelib}/*
#%{_bindir}/*

