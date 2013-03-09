Summary:	CD ripper aiming for accuracy over speed
Name:		morituri
Version:	0.2.0
Release:	2
License:	GPL v3
Group:		Applications
Source0:	http://thomas.apestaart.org/download/morituri/%{name}-%{version}.tar.bz2
# Source0-md5:	0766778054ff9fbb98effd08130c7e98
URL:		http://thomas.apestaart.org/thomas/trac/wiki/DAD/Rip
BuildRequires:	python
BuildRequires:	rpm-pythonprov
Requires:	cdparanoia-III
Requires:	cdrdao
Requires:	gstreamer010-plugins-base
Requires:	python-gstreamer010
Requires:	python-musicbrainz2
Requires:	python-setuptools
# see https://github.com/thomasvs/morituri/issues/5
# Suggests:	python-pycdio
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
morituri is a CD ripper aiming for accuracy over speed.
Its features are modeled to compare with Exact Audio Copy on Windows.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/rip
%{py_sitescriptdir}/%{name}
%{_mandir}/man1/rip.1*

