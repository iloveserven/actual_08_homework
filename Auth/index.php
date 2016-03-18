<?php
header('Content-type: text/json');

// define('CAS_ROOT_DIR', dirname(__FILE__)); 
require_once "./User.class.php";


if (isset($_REQUEST['method'])) {
	$method = $_REQUEST['method'];
	User::casInit();

	if ($method == "isAuthenticated") {
		// check CAS authentication
		$auth = phpCAS::checkAuthentication();
		if ($auth) {
				$data = array(
					"errno" => 0,
					"errMsg" => "",
					"data" => "true"
					);
		} else {
				$data = array(
					"errno" => 0,
					"errMsg" => "",
					"data" => false
					);
		}
		echo json_encode($data);
	} else {
		$data = array(
			"errno" => 2,
			"errMsg" => "未知的接口",
			"data" => null
			);
		echo json_encode($data);
	}

} else {
	$data = array(
		"errno" => 1,
		"errMsg" => "请访问正确的接口",
		"data" => null
		);
	echo json_encode($data);
}
?>
