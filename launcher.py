import wx
 
class Panel1(wx.Panel):
    def __init__(self, parent, id):
        #Create panel
        wx.Panel.__init__(self, parent, id)

        # Instantiate variable used to represent the input file. The file itself can be of one of the following types: .bmp, .gif, .jpeg, .png
        image_file = 'AGS.png'
        # Convert input to bitmap to be held in memory during execution of the program.
        bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        # Anchor image's upper left corner at panel origin.
        self.bitmap1 = wx.StaticBitmap(self, -1, bmp1, (0, 0))
        
        # Binds button to background image. The background image (Bitmap1) is the parent of all subsequent elements.
        self.button1 = wx.Button(self.bitmap1, id=-1, label='Button1', pos=(600, 600))
 
app = wx.App()
#Variables utilized by the subsequently created frame go here.
Title = 'Test'

#Create Frame.
frame1 = wx.Frame(None, 0, title=Title, size=(300, 400))
frame1.SetBackgroundColour(wx.BLUE)

#Marry the panel to the frame and display them accordingly.
panel1 = Panel1(frame1, 0)
frame1.Show(True)
app.MainLoop()