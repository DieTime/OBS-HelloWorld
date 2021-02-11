Name:       OBS-HelloWorld
Summary:    Training OBS hello world app
Version:    1.0.0
BuildRequires:  cmake

%package -n obs-service-tar-git
Requires: git
Requires: obs-source_service
Summary: OBS source service to generate sources from git
%description -n obs-service-tar-git
This package provides the service to generate source from git inside an OBS source service

%description
Test OBS package with Hello World program

%prep
%setup -q

%build
%cmake_build

%install
%make_install

%files
%{_bindir}/%{name}
