#
# spec file for package python-fido2
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define python_version python3
%bcond_without test
%define modname fido2
Name:           python3-fido2
Version:        0.9.1
Release:        0
Summary:        Python-based FIDO 2.0 library
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/Yubico/python-fido2
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  python3-cryptography
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  fdupes
BuildRequires:  python3-rpm-macros
Requires:       python3-cryptography >= 1.5
Requires:       python3-six

%description
This library supports the FIDO U2F and FIDO 2.0 protocols for communicating
with a USB authenticator via the Client-to-Authenticator Protocol (CTAP 1 and 2).
In addition to this low-level device access, classes defined in the fido2.client
implement higher level device operations.

%prep
%setup -q -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install

%files
%doc NEWS* README*
%license COPYING*
%{python3_sitelib}/*

%changelog
