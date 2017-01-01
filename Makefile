NAME := arena-tracker
SPEC := $(NAME).spec
DIST := dist
SRCS := $(DIST)/SOURCES

rpm: clean
	mkdir -p $(DIST)/{BUILD,BUILDROOT,RPMS,SPECS,SOURCES,SRPMS}
	spectool -g -s 0 -f -C $(SRCS) $(SPEC)
	cp -pf *.ico $(SRCS)
	cp -pf *.desktop $(SRCS)
	rpmbuild -ba \
		--define "_topdir $(PWD)/$(DIST)" \
		$(SPEC)

lint:
	rpmlint $(SPEC)

clean:
	rm -rf $(DIST)

install:
	sudo dnf install $(DIST)/RPMS/x86_64/$(name).*.rpm
