import os

os.environ.get('FACEBOOK')

def site_settings_processor(request):
	context_dictionary = {
		'root_url': 'jpark.pythonanywhere.com',
		'admin_name': 'admin',
		'company_name': 'TerraPro, Inc',
		'company_short': 'TerraPro',
		'logo_file_name': 'images/logo.jpg',
		'site_email': 'james@terrapro.com',
		# if email changes, update misc_pages/email.html
		'company_phone_text': '480-444-8776',
		'company_phone_link': '14804448776',
		'company_fax': '480-452-0347',
		'company_address': '',
		'yelp_id': '',
		'meta_content': 'Phoenix area landscape maintenance professionals. 30 years and going strong.',
		'navbar_link1_name': 'home',
		'navbar_link1_text': 'Home',
		'navbar_link2_name': 'about',
		'navbar_link2_text': 'About',
		'navbar_link3_name': 'services',
		'navbar_link3_text': 'Services',
		'navbar_link4_name': 'contact',
		'navbar_link4_text': 'Contact',
	}
	return(context_dictionary)