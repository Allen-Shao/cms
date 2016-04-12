# generate Python documentation
make -C docs html
# generate JavaScript documentation
jsdoc cmsapp/static/js -d docs/jsdoc
