<?php
require_once "./Config.class.php";
require_once Config::phpcas_path . '/CAS.php';

class User {
	public static function casInit() {
		// Enable debugging
		phpCAS::setDebug();
	  // Enable verbose error messages. Disable in production!
		phpCAS::setVerbose(true);
	  // Initialize phpCAS
	  phpCAS::client(CAS_VERSION_2_0, Config::cas_host , Config::cas_port , Config::cas_context, true);
		// For quick testing you can disable SSL validation of the CAS server.
		// THIS SETTING IS NOT RECOMMENDED FOR PRODUCTION.
		// VALIDATING THE CAS SERVER IS CRUCIAL TO THE SECURITY OF THE CAS PROTOCOL!
	  phpCAS::setNoCasServerValidation();
	}
}
?>
