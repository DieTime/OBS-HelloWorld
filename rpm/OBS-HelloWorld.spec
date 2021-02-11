%define build_folder ./cmake-build

Name:       OBS-HelloWorld
Summary:    Training OBS hello world app
Version:    1.0.0
BuildRequires:  cmake

%description
Test OBS package with Hello World program

%prep
%setup -q

%build
%cmake_build

%install
%cmake_install

%files
%{_bindir}/%{name}
