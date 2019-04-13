#!/usr/bin/python36
import cgi
import cgitb
cgitb.enable()

print("content-type:text/html")
print("\n")
html="""
<!DOCTYPE html>
<html lang="en" class="no-js">
	<head>
		<meta charset="UTF-8" />
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> 
		<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
		<title>Welcome to SaaS</title>
		
			
		<link rel="stylesheet" type="text/css" href="/var/www/html/minor2/client/css/normalize.css" />
		<link rel="stylesheet" type="text/css" href="/var/www/html/minor2/client/css/demo.css" />
		<link rel="stylesheet" type="text/css" href="/var/www/html/minor2/client/css/component2.css" />
		

		<script src="/var/www/html/minor2/client/js/modernizr-2.6.2.min.js"></script>
		<script>
			function showServices()
			{
				path='a.html'		
				document.getElementById("services").href=path
			}
		</script>

	</head>
	<body>
		<div class="container">
			<!-- Top Navigation -->
			
			<header>
				<h1>CLP Incorporation <span>Providing Software Solutions Online 24/7 </span></h1>	<br/><br/>
				<nav >
					<div class="type-3">
						<a href="/var/www/cgi-bin/minor2/url.py" class="btn btn-3">
							<span class="txt">VLC</span>
							<span class="round"></span>
						</a>
						<a href="" class="btn btn-3">
							<span class="txt">Splunk</span>
							<span class="round"></span>
						</a>
					</div>
				</nav>
	
			</header>
			<div class="component">
				<h2>Software as a Service</h2>
				 <!--Start Nav Structure -->
				<button class="cn-button" id="cn-button">Menu</button>
				<div class="cn-wrapper" id="cn-wrapper">
					<ul>
						<li><a href="#"><span></span></a></li>
						<li><a href="#"><span> </span></a></li>
						<li><a href="#"><span>My Profile</span></a></li>
						<li><a href="" id="services" onclick="showServices()" target="f1"><span>My Services</span></a></li>
						<li><a href="#"><span>Billing</span></a></li>
						<li><a href="#"><span></span></a></li>
						<li><a href="#"><span></span></a></li>
					 </ul>
				</div>
				<!-- End of Nav Structure -->
			</div>
			<section>
				<!--<iframe name="f1" width="100%" height="800px" frameborder=0 src="/var/www/html/minor2/client/initial.html">
				</iframe> -->
			</section>
		</div><!-- /container -->
		<script src="/var/www/html/minor2/client/js/polyfills.js"></script>
		<script src="/var/www/html/minor2/client/js/demo2.js"></script>
		

	</body>
</html>"""
print(html)
