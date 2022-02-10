<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'eyeflight' );

/** MySQL database username */
define( 'DB_USER', 'Thomas' );

/** MySQL database password */
define( 'DB_PASSWORD', 'Dominique2002*' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '7z]DD)Y5Iqu!+EDyy-nw(Y%o##=rZ=]%o<;64J*&DPt(4pMt;1b7s;6&97)R b!u' );
define( 'SECURE_AUTH_KEY',  'yn#FWa{;<0Yb|:i*oKy9X|M.Q<0ASTy9Dv}Rsy]BZ^sHHt_]5qMzhPHv@5G}M]zd' );
define( 'LOGGED_IN_KEY',    'tpETmTJk+KGR1:>^x$cq<*xM>TR1ez9wf$L1SH;oN9Zp0&w|OCTDz*$Fol2@L?]+' );
define( 'NONCE_KEY',        '%x*KzYh2^k]*jtDC-EEtr/J]+z!ImqO,jzNY`@x},%kM`Fbh2/(we/=o)tb+oJW_' );
define( 'AUTH_SALT',        '`T_YGn,&K/Cw8z$~bL7q>nFp%[2PjvH^O5sBPD3zN9A:QzP%y,K(,C6}$})^EB=6' );
define( 'SECURE_AUTH_SALT', 'JMZ6Q>,o*e?&afNb..GMc >^WCc/vq@b.l }RAmD^=V J~=zm@yw2*{8:UBK&z+=' );
define( 'LOGGED_IN_SALT',   'zVS@TJUNJjU5+P_!,N-(j-UoT*;XEQB8`tw%g5@6KhipasI:_Is:UxS>|tA=_:Ah' );
define( 'NONCE_SALT',       '5p3J~7QaZZ*$<`_6|lM*TPY/--:? LY9ldg6)V|+=JX+W3rrhe)^1-Ur=.%Cnelm' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
