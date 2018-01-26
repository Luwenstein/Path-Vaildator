import wx, os, time
from sys import argv

current_dir = sys.argv[1] # Get current directory

class windowClass(wx.Frame):
    
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, None, -1, 'Quick FS', size=(360,360), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        
        panel = wx.Panel(self, -1) # Make Sure that this looks correct on all platforms
        
        # Main GUI Elements
        
        # Scroll Back Log
        self.detailBox = wx.TextCtrl(panel, wx.ID_ANY, pos=(5,20), size=(300,250), style=wx.TE_RICH2 | wx.TE_READONLY | wx.TE_MULTILINE)
        
        # Static Text

        self.Status = wx.StaticText(panel, wx.ID_ANY, 'Stats:', (10,3))
        self.S_passed = wx.StaticText(panel, wx.ID_ANY, '0 Passed', (10,280))
        self.S_failed = wx.StaticText(panel, wx.ID_ANY, '0 Failed', (90,280))
        
        self.failed_count = 0 # How many times a path failed and passed
        self.passed_count = 0 #
        
        # Buttons
        
        self.button0=wx.Button(panel, label='Retry', pos=(250,280))
        self.Bind(wx.EVT_BUTTON, self.Retry, self.button0) # Run the Retry function when button is pressed
        
        self.SetTitle('Path Validator V1.0')
        self.Show(True)

        time.sleep(2) # Have to add delay so window can load correctly
        self.Validator(current_dir)
    
    def Validator(self, current_dir):
        """Groups everything"""
        self.button0.Disable()
        c_dir = os.path.abspath(current_dir)
        allChildren = [x[0] for x in os.walk(c_dir)] # have to change because root dir is not included
        
        self.Validate(" ", c_dir) # validate mother directory
        for folder in allChildren:
                cachefiles_Folders = os.listdir(folder)
                self.Validate(cachefiles_Folders, folder)
        self.button0.Enable()
        
        
            
    def Validate(self, files_Folders, c_dir):
        
        for path in files_Folders:
            
            if len(c_dir+'/'+path) <= 255: # 255 to add 1 character Buffer
                self.detailBox.WriteText(c_dir+'\\'+path)
                self.detailBox.SetDefaultStyle(wx.TextAttr(wx.GREEN))
                self.detailBox.WriteText("  Passed...\n\n")
                self.detailBox.SetDefaultStyle(wx.TextAttr(wx.BLACK))
                self.passed_count += 1
            elif len(c_dir+'/'+path) > 255:
                self.detailBox.WriteText(c_dir+'\\'+path+'  ')
                self.detailBox.SetDefaultStyle(wx.TextAttr(wx.RED))
                self.detailBox.WriteText("Failed...\n\n")
                self.detailBox.SetDefaultStyle(wx.TextAttr(wx.BLACK))
                self.failed_count += 1
                
        self.S_failed.SetLabel(str(self.failed_count)+' Failed')
        self.S_passed.SetLabel(str(self.passed_count)+' Passed')
        time.sleep(0.005) # puts on a bit of a brake
        
    def Retry(self, event):
        self.button0.Disable() # Disable Retry button to prevent user from spamming it
        self.failed_count = 0
        self.passed_count = 0
        self.detailBox.SetValue('')
        self.Validator(current_dir)

if __name__ == "__main__":
    app = wx.App()
    frame = windowClass()
    frame.Show()
    app.MainLoop()


