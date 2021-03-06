Summary:	CD ripper aiming for accuracy over speed
Name:		morituri
Version:	0.2.3
Release:	4
License:	GPL v3
Group:		Applications
Source0:	http://thomas.apestaart.org/download/morituri/%{name}-%{version}.tar.bz2
# Source0-md5:	9587255fc9b357942e700b9fda4c6ddf
Patch0:		%{name}-freddix.patch
URL:		http://thomas.apestaart.org/thomas/trac/wiki/DAD/Rip
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	python
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
Requires:	cdparanoia-III
Requires:	cdrdao
Requires:	gstreamer010-plugins-good
Requires:	python-cddb
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
# tune vorbis encoding a bit
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/morituri/plugins

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/rip
%{py_sitescriptdir}/%{name}
%{_libdir}/morituri/plugins
%{_mandir}/man1/rip.1*

