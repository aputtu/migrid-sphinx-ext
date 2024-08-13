# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


./.venv/pyvenv.cfg:
	@echo "provisioning environment"
	@/usr/bin/env python3 -m venv ./.venv

.PHONY: dependencies
dependencies: ./.venv/pyvenv.cfg ./requirements.txt
	@echo "installing dependencies"
	@./.venv/bin/pip3 install -r ./requirements.txt

./requirements.txt:
	@


.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

