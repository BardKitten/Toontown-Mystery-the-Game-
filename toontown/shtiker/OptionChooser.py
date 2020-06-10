from direct.gui.DirectGui import *

class OptionChooser:
    
    def __init__(self, book, labelText, row, indexCommand, extraArgs, exitCommand):
        options_text_scale = 0.052
        leftMargin = -0.72
        buttonbase_xcoord = 0.35
        textStartHeight = 0.45
        textRowHeight = 0.145
        y = textStartHeight - row * textRowHeight
        matGui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui')
        arrow_image = (matGui.find('**/tt_t_gui_mat_shuffleArrowUp'), matGui.find('**/tt_t_gui_mat_shuffleArrowDown'))

        self.indexCommand = indexCommand
        self.extraArgs = extraArgs
        self.exit = exitCommand
        self.label = DirectLabel(book, relief=None, text=labelText, text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, y))
        self.display = DirectLabel(book, relief=None, scale=0.06, text_wordwrap=9, pos=(buttonbase_xcoord, 0, y))
        self.leftButton = DirectButton(book, relief=None, image=arrow_image, scale=0.45, pos=(textStartHeight - 0.4, 0, y), command=self.offsetIndex, extraArgs=[-1])
        self.rightButton = DirectButton(book, relief=None, image=arrow_image, scale=-0.45, pos=(textStartHeight + 0.2, 0, y), command=self.offsetIndex, extraArgs=[1])
        self.index = -1
        matGui.removeNode()
    
    def unload(self):
        self.label.destroy()
        del self.label
        self.display.destroy()
        del self.display
        self.leftButton.destroy()
        del self.leftButton
        self.rightButton.destroy()
        del self.rightButton
    
    def offsetIndex(self, offset):
        self.index += offset
        self.indexCommand(*self.extraArgs)
    
    def setIndex(self, index):
        self.index = index
    
    def setDisplayText(self, text):
        self.display['text'] = text
    
    def setDisplayFont(self, font):
        self.display['text_font'] = font
    
    def decideButtons(self, minCount, maxCount):
        if self.index <= minCount:
            self.leftButton.hide()
        else:
            self.leftButton.show()

        if self.index >= maxCount:
            self.rightButton.hide()
        else:
            self.rightButton.show()