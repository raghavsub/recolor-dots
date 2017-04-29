/* user and group to drop privileges to */
static const char *user  = "raghav";
static const char *group = "raghav";

static const char *colorname[NUMCOLS] = {
	[INIT] =   "#000000",   /* after initialization */
	[INPUT] =  "#{{base00}}",   /* during input */
	[FAILED] = "#{{base08}}",   /* wrong password */
};

/* treat a cleared input like a wrong password (color) */
static const int failonclear = 1;
