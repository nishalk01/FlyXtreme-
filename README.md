# FlyXtreme

<b> None of these codes are mine, but are modified versions or the original versions of code borrowed from other repositories
</b>
<b> The repository "combined" consists of 3 python script </b> 
<ul>
<li> camera.py </li>
<li> detect.py </li>
 <li>video_main.py</li>
</ul>
 <h4>camera.py</h4>
  <div>-->Starts the camera through cv2 VideoCapture. It also consists of defination<i>  _del_ </i>that stops the camera and the  <i>get_frame()</i> function reads the frames from the camera that has been previously started.</div>
 <h4>detect.py</h4>-->Returns the rectangle coordinates along with the classname. Uses MobileNetSSDv2 for object detection.
 <h4>video_main.py</h4>-->takes the input from camera.py(the frames) and rectangle coordinates(for detect.py) and pushes the image onto a local host.
 
 <h1>How to run</h1>
 <ul>
 <li>Make sure you have all the modules that are required installed in your machine.</li>
 <li>Download the zip or clone the repository</li>
 <li>Make sure u have downloaded the model "frozen_inference_graph.pb" and "frozen_inference_graph.pb" from the link given below</li>
 <li>Copy the .pb and .pbtxt on the same location where the scripts are present</li>
 <li>Before running the scripts make sure u change ur public ip in host(video_main.py) <b>use the command <i>ifconfig</i> for windows</b> or <b>use the command <i>ip addr show</i> on linux </b></li>
 <li>Run the command(make sure the terminal is open in the location your scripts are present)</li>
 </ul>
<h2> python video_main.py </h2>
 <b> the website-insteraction is about the part that involves updating the site with video and also for the part where the python script has to pass data onto the website(which will be mainly helpful while using google maps api).This folder is ongoing .</b>
 
<b> Reference: </b>
<ul>
 <li><link>https://jeanvitor.com/tensorflow-object-detecion-opencv/</link></li>
 <li><link>https://www.w3schools.com/bootstrap/bootstrap_theme_company.asp</link></li>
 </ul>
