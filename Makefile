# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = _build
PUBLISHDIR	  = Publish_CIM
SHRPTBUILDDIR=$(PUBLISHDIR)/Richelin-KnowledgeBase-aspx
SHRPTBUILDDIR2=$(PUBLISHDIR)/Richelin-KnowledgeBase-html
SHRPTBUILDDIR3=$(PUBLISHDIR)/Richelin-KnowledgeBase-pdf
EMBED_AT_CIM_PROJNAME=__Wiki_EmbeddedAtCIM

# List all the directory you don't want to publish here
TEMP_DIRS=$(SHRPTBUILDDIR)/html/KnowledgeBase/$(EMBED_AT_CIM_PROJNAME)/_Logs_Journal \
               $(SHRPTBUILDDIR2)/html/KnowledgeBase/$(EMBED_AT_CIM_PROJNAME)/_Logs_Journal \
               $(SHRPTBUILDDIR)/html/_sources \
               $(SHRPTBUILDDIR2)/html/_sources 

SLIDE_DIR	  = $(BUILDDIR)/slides
# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

livehtml:
	sphinx-autobuild --delay 15  -t personal "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

publish: post_build_cleanup
	@echo "done creating publish documents"

sharepoint-build: Makefile 
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(SHRPTBUILDDIR)" $(SPHINXOPTS) $(O) -D html_file_suffix=".aspx"
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(SHRPTBUILDDIR2)" $(SPHINXOPTS) $(O)
	@$(SPHINXBUILD) -M pdf "$(SOURCEDIR)" "$(SHRPTBUILDDIR3)" $(SPHINXOPTS) $(O)

post_build_cleanup: sharepoint-build
	for dir in $(TEMP_DIRS) ; do \
		rm -rf $$dir ; \
	done

sharepoint-clean: Makefile 
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(SHRPTBUILDDIR)" $(SPHINXOPTS) $(O)
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(SHRPTBUILDDIR2)" $(SPHINXOPTS) $(O)
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(SHRPTBUILDDIR3)" $(SPHINXOPTS) $(O)

slides:
	$(SPHINXBUILD) -b slides "$(SOURCEDIR)" $(ALLSPHINXOPTS) $(SLIDE_DIR)
	@echo "Build finished. The HTML slides are in $(SLIDE_DIR)"