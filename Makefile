# This Makefile is a modified version of the original version PyGTK Tutorial Makefile.
# Credits go to the developers.

CSSFILE = style.css
XSLFILES = common.xsl devhelp.xsl html.xsl pdf-dblatex.xsl pdf-style.xsl pdf.xsl tut-html-style.xsl
TUTORIALLINKS = tutorial/resources tutorial/examples
TUTORIALXMLFILES = \
source/aboutdialog.xml \
source/actionobjects.xml \
source/adjustment.xml \
source/alignment.xml \
source/arrow.xml \
source/assistant.xml \
source/boxes.xml \
source/buttonbox.xml \
source/buttonwidgets.xml \
source/calendar.xml \
source/cellrendererwidgets.xml \
source/cellview.xml \
source/clipboard.xml \
source/colorselectionwidgets.xml \
source/comboboxentry.xml \
source/combobox.xml \
source/commonmethods.xml \
source/contents.xml \
source/curve.xml \
source/dialog.xml \
source/drawingarea.xml \
source/entrycompletion.xml \
source/entry.xml \
source/eventbox.xml \
source/expander.xml \
source/filefilter.xml \
source/fileselectionwidgets.xml \
source/fixed.xml \
source/fontselectionwidgets.xml \
source/framewidgets.xml \
source/gammacurve.xml \
source/gettingstarted.xml \
source/gtkmainloop.xml \
source/handlebox.xml \
source/iconview.xml \
source/image.xml \
source/infobar.xml \
source/inputdialog.xml \
source/introduction.xml \
source/label.xml \
source/layout.xml \
source/liststore.xml \
source/menuconstruction.xml \
source/messagedialog.xml \
source/notebook.xml \
source/packingtheory.xml \
source/pane.xml \
source/plugsocket.xml \
source/progressbar.xml \
source/recentchooserwidgets.xml \
source/ruler.xml \
source/scalebutton.xml \
source/scale.xml \
source/scrollbar.xml \
source/scrolledwindow.xml \
source/selectionwidgets.xml \
source/separator.xml \
source/signaltheory.xml \
source/sizegroup.xml \
source/spinner.xml \
source/statusbar.xml \
source/statusicon.xml \
source/stockimages.xml \
source/table.xml \
source/textviewconstruction.xml \
source/toolbar.xml \
source/toolitemwidgets.xml \
source/tooltip.xml \
source/treestore.xml \
source/treeviewconstruction.xml \
source/uimanager.xml \
source/unavailabledeprecated.xml \
source/viewport.xml \
source/volumebutton.xml \
source/window.xml

# Commands to run to generate documentation files
tutorial-html: tutorial ${TUTORIALLINKS} ${TUTORIALXMLFILES} ${CSSFILE}
	cp ${CSSFILE} tutorial-html/
	xsltproc --nonet --xinclude -o tutorial-html/ --stringparam gtkdoc.bookname tutorial tut-html-style.xsl source/contents.xml

tutorial-pdf: tutorial ${TUTORIALLINKS} ${TUTORIALXMLFILES} ${XSLFILES}
	cp source/*.xml tutorial-pdf/ 
	dblatex --pdf -T db2latex -p pdf-dblatex.xsl -o pygtktutorial.pdf source/contents.xml

tutorial-dist:
	tar zhcf pygtktutorial-html.tar.gz tutorial-html

tutorial-src:
	tar zcf pygtktutorial-src.tar.gz ${TUTORIALXMLFILES} ${XSLFILES} ${CSSFILE} Makefile examples resources

# Creates new directories if needed
tutorial:
	-mkdir tutorial-html
	-mkdir tutorial-pdf

tutorial/resources:
	-mkdir tutorial-html/resources
	-(cd tutorial-html/resources; cp ../../resources/* .)

tutorial/examples:
	-mkdir tutorial-html/examples
	-(cd tutorial-html/examples; cp ../../examples/* .)

clean:
	-rm -rf tutorial-html/ tutorial-pdf/ pygtktutorial.pdf pygtktutorial-src.tar.gz pygtktutorial-html.tar.gz
