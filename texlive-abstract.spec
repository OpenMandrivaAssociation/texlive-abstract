# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/abstract
# catalog-date 2009-09-02 11:33:10 +0200
# catalog-license lppl
# catalog-version 1.2a
Name:		texlive-abstract
Version:	1.2a
Release:	12
Summary:	Control the typesetting of the abstract environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/abstract
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abstract.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abstract.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abstract.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The abstract package gives you control over the typesetting of
the abstract environment, and in particular provides for a one
column abstract in a two column paper.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/abstract/abstract.sty
%doc %{_texmfdistdir}/doc/latex/abstract/README
%doc %{_texmfdistdir}/doc/latex/abstract/abstract.pdf
#- source
%doc %{_texmfdistdir}/source/latex/abstract/abstract.dtx
%doc %{_texmfdistdir}/source/latex/abstract/abstract.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2a-2
+ Revision: 749044
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2a-1
+ Revision: 717784
- texlive-abstract
- texlive-abstract
- texlive-abstract
- texlive-abstract
- texlive-abstract

