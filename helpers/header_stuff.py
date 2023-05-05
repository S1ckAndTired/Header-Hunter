mind_headers = ["X-Frame-Options", "X-Content-Type-Options", "Referrer-Policy", "Strict-Transport-Security", "Content-Security-Policy", "Permissions-Policy", "X-XSS-Protection", "Access-Control-Allow-Origin"]

disclosure = ["Server", "X-Powered-By", "X-AspNet-Version", "X-AspNetMvc-Version"]

exposed = {}
missing = []
info_disc = []
casual_headers = []
on_the_fly = {}
