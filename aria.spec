Summary:	Download tool similar to Reget or GetRight
Summary(pl):	Narzêdzie do pobierania plików podobne do GetRighta
Name:		aria
Version:	1.0.0
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://aria.rednoah.com/storage/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	e4e968fd10f3beb2402b851f5dad74ff
Patch0:		%{name}-gettext.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-gcc.patch
URL:		http://aria.rednoah.com/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib-devel >= 1.2.6
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aria is a download tool similar to Reget or GetRight. It downloads
files from Internet via HTTP or FTP. The transfer can be paused,
resumed, queued and saved. It has very friendy GTK+ based GUI, and
useful log consoles.Program supports CRC checking, HTTP proxy server,
cut-and-paste, drag-and-drop, and can define specific file retrieving
procedure for particular web servers.

%description -l pl
Aria jest narzêdziem do pobierania plików podobnym do Reget lub
GetRight. Aria pobiera pliki z Internetu poprzez HTTP lub FTP.
Transfer mo¿e byæ wstrzymany, wznowiony, zakolejkowany i zapisany.
Program ma przyjazny interfejs u¿ytkownika bazuj±cy na GTK+ oraz
u¿yteczne logi. Program wspiera sprawdzanie sum CRC, obs³ugê HTTP
proxy, skopiuj-i-wklej, przeci±gnij-i-upu¶æ oraz umo¿liwia definiowane
specjalnych zachowañ przy pobieraniu plików z okre¶lonych serwerów.

%prep
%setup -q
%patch0 -p1
tail -n +937 aclocal.m4 > acinclude.m4
%patch1 -p1
%patch2 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/aria
