%define build_folder ./cmake-build

Name:       OBS-HelloWorld
Summary:    Training OBS hello world app
Version:    1.0.0
BuildRequires:  cmake

%build
cmake -DCMAKE_BUILD_TYPE=Release -S . -B %{build_folder}
cmake --build %{build_folder} --config Release

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{build_folder}/%{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
