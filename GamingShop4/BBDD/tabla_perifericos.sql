-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-04-2020 a las 19:17:07
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_gaming_shop`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_perifericos`
--

CREATE TABLE `tabla_perifericos` (
  `id` int(11) NOT NULL,
  `tipo` varchar(255) NOT NULL,
  `marca` varchar(255) NOT NULL,
  `modelo` varchar(255) NOT NULL,
  `gama` varchar(255) NOT NULL,
  `precio` decimal(6,2) NOT NULL,
  `soporte` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_perifericos`
--

INSERT INTO `tabla_perifericos` (`id`, `tipo`, `marca`, `modelo`, `gama`, `precio`, `soporte`) VALUES
(7, 'Display', 'Alienware', '25 AW2518H', 'Basic', '534.82', 0),
(3, 'Gaming Chair', 'Corsair', 'T2 ROAD WARRIOR', 'Advance', '339.90', 0),
(4, 'Headset', 'Corsair', 'VIRTUOSO RGB WIRELESS SE', 'Elite', '209.99', 0),
(14, 'Gaming Chair', 'Noblechairs', 'Hero Gaming Chair', 'Elite', '680.90', 0),
(1, 'Mouse', 'Razer', 'Viper Ultimate', 'Elite', '169.99', 0),
(6, 'Accesory', 'Razer', 'Firefly V2', 'Elite', '59.99', 0),
(8, 'Mouse', 'Razer', 'Viper', 'Advance', '89.99', 0),
(10, 'Wireless Audio', 'Razer', 'Hammerhead True Wireless Earbuds ', 'Advance', '119.99', 0),
(13, 'Mouse', 'Razer', 'Basilisk Ultimate Wireless RGB', 'Elite', '169.99', 0),
(15, 'Keyboard', 'Razer', 'BlackWidow Elite', 'Basic', '179.99', 0),
(2, 'Keyboard', 'Roccat', 'Vulcan 122 AIMO', 'Advance', '160.90', 0),
(9, 'Headset', 'Roccat', 'Khan AIMO', 'Advance', '107.99', 0),
(16, 'Headset', 'Roccat', 'Score', 'Basic', '38.95', 1),
(5, 'Mouse', 'ROG', 'GLADIUS II WIRELESS RGB', 'Basic', '86.99', 0),
(11, 'Display', 'ROG', 'Swift PG27UQ', 'Elite', '2049.80', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tabla_perifericos`
--
ALTER TABLE `tabla_perifericos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tabla_perifericos`
--
ALTER TABLE `tabla_perifericos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
