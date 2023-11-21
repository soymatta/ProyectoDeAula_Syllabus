-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-11-2023 a las 20:15:29
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `syllabus`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contents_and_strategies`
--

CREATE TABLE `contents_and_strategies` (
  `id` int(11) NOT NULL,
  `content_name` varchar(50) NOT NULL,
  `sub_content` text DEFAULT NULL,
  `strategies` text DEFAULT NULL,
  `syllabi_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `contents_and_strategies`
--

INSERT INTO `contents_and_strategies` (`id`, `content_name`, `sub_content`, `strategies`, `syllabi_id`) VALUES
(1, 'Ingeniería de Sistemas', 'o Jerarquía de la Ingeniería de Software\r\no Ingeniería de procesos de negocios\r\no Ingeniería del producto\r\no Modelado del Sistema', ' Talleres en clase, \r\n Ejercicios en clase, \r\n Quices, \r\n Trabajo independiente del estudiante, \r\n Participación del estudiante, \r\n Examen individual\r\n Exposiciones\r\n', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `evaluations`
--

CREATE TABLE `evaluations` (
  `id` int(11) NOT NULL,
  `first_percentage` int(11) NOT NULL,
  `description_first_percentage` text DEFAULT NULL,
  `second_percentage` int(11) NOT NULL,
  `description_second_percentage` text DEFAULT NULL,
  `third_percentage` int(11) NOT NULL,
  `description_third_percentage` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `evaluations`
--

INSERT INTO `evaluations` (`id`, `first_percentage`, `description_first_percentage`, `second_percentage`, `description_second_percentage`, `third_percentage`, `description_third_percentage`) VALUES
(1, 30, 'Evaluación formativa (20%): Talleres, exposiciones, Quices\r\nParcial teórico (25%) y práctico (25%)\r\nProyecto de aula (30%)', 30, 'Evaluación formativa (20%): Talleres, exposiciones, Quices\r\nParcial teórico (25%) y práctico (25%', 40, 'Evaluación formativa (20%): Talleres, exposiciones, Quices\r\nParcial teórico (25%) y práctico (25%)\r\nProyecto de aula (30%)\r\n');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `faculties`
--

CREATE TABLE `faculties` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `faculties`
--

INSERT INTO `faculties` (`id`, `name`) VALUES
(1, 'Ingeniería');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `faculties_subjects`
--

CREATE TABLE `faculties_subjects` (
  `id` int(11) NOT NULL,
  `faculties_id` int(11) NOT NULL,
  `subjects_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `faculties_subjects`
--

INSERT INTO `faculties_subjects` (`id`, `faculties_id`, `subjects_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `subjects`
--

CREATE TABLE `subjects` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `modality` enum('presencial','presencial-tic','virtual') NOT NULL,
  `type` enum('practica','teorica','teorico-practica') NOT NULL,
  `credits` int(11) NOT NULL,
  `semester` varchar(2) NOT NULL,
  `bibliography` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `subjects`
--

INSERT INTO `subjects` (`id`, `name`, `modality`, `type`, `credits`, `semester`, `bibliography`) VALUES
(1, 'Ingeniería del Software II', 'presencial', 'teorica', 2, '1', NULL),
(2, 'Programación Web', 'presencial', 'practica', 2, '2', NULL),
(3, 'Metodos numericos', 'presencial', 'teorico-practica', 4, '3', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `syllabi`
--

CREATE TABLE `syllabi` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `program` varchar(50) DEFAULT NULL,
  `cycle` varchar(50) DEFAULT NULL,
  `justification` text DEFAULT NULL,
  `competences` text DEFAULT NULL,
  `learning_results` text DEFAULT NULL,
  `methodology` text DEFAULT NULL,
  `evaluations_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL,
  `faculty_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `syllabi`
--

INSERT INTO `syllabi` (`id`, `date`, `program`, `cycle`, `justification`, `competences`, `learning_results`, `methodology`, `evaluations_id`, `subject_id`, `faculty_id`) VALUES
(1, '2023-11-21 13:49:53', 'INGENIERÍA DE SISTEMAS', 'PROFESIONAL', 'Después de revisar y aplicar los conceptos previos de las fases de Ingeniería de Software (Análisis \r\ny Diseño de Sistemas), es indispensable para el estudiante comprender y desarrollar mecanismos \r\npara construir e implementar la aplicación que permitirá solucionar los problemas identificados \r\nen la fase de análisis y convertir las estructuras definidas en la fase de diseño en una solución \r\npráctica, probada y documentada lista para ser usada por los usuarios', ' Competencias básicas: Comunicar asertivamente las diferentes propuestas para dar solución a \r\nlas necesidades organizacionales que enfrenta el ingeniero de sistemas.\r\n Competencias genéricas: Reconocer y respetar los puntos de vistas y opiniones de otros \r\nmiembros del grupo y llegar a acuerdos, para obtener los mejores resultados trabajando en \r\nequipo.\r\n Competencias específicas: Diseñar, Desarrollar, seleccionar y evaluar aplicaciones y sistemas \r\ninformáticos, asegurando su fiabilidad, seguridad y calidad conforme a los principios éticos y a la \r\nlegislación y normativa vigente.\r\n Competencias específicas: Identificar estándares para creación de prototipos en interfaces de \r\nusuarios\r\n Competencias específicas: Identificar los diferentes tipos de pruebas que se le deben realizar a \r\nlos sistemas de información para diseñar y aplicar el plan de pruebas.\r\n Competencias específicas: Identificar las pautas de documentación para la construcción de un \r\nsistema de información', 'RA_4:\r\nComunica efectivamente en forma oral, gráfica y por escrito usando un lenguaje técnico.\r\nRA_7:\r\nDiseña procesos, productos y servicios basados en tecnología, software e información para el \r\nbeneficio de los diferentes sectores socioeconómicos.\r\nRA_8:\r\nAnaliza criterios de selección y configura plataformas tecnológicas para el desarrollo y ejecución de \r\naplicaciones y servicios informáticos.\r\nRA_10:\r\nAplica técnicas, principios y herramientas para el desarrollo de habilidades que fortalezcan el \r\naprendizaje autónomo', 'RABAJO PRESENCIAL\r\nLos conocimientos de la asignatura se adquieren a través del estudio razonado de todas las \r\nunidades didácticas de la asignatura, previa presentación del docente, ejemplos y ejercicios \r\nen clases, así como del material didáctico que se ponga a disposición de los estudiantes en \r\nla plataforma Moodle.\r\nTRABAJO INDEPENDIENTE\r\nLos estudiantes tendrán talleres y trabajos prácticos e investigativos sobre los temas vistos \r\nen clases que puedan realizar durante las horas independientes asignadas para la materia.', 1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `role` enum('admin','teacher') NOT NULL,
  `status` tinyint(1) NOT NULL,
  `faculty_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `role`, `status`, `faculty_id`) VALUES
(1, 'Decanatura', 'decanatura-baq@unilibre.edu.co', 'decanatura', 'admin', 1, 1),
(2, 'Rol teacher', 'teacher@unilibre.edu.co', 'teacher', 'teacher', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users_subjects`
--

CREATE TABLE `users_subjects` (
  `id` int(11) NOT NULL,
  `users_id` int(11) NOT NULL,
  `subjects_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `users_subjects`
--

INSERT INTO `users_subjects` (`id`, `users_id`, `subjects_id`) VALUES
(1, 2, 2),
(2, 2, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users_syllabi`
--

CREATE TABLE `users_syllabi` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `syllabi_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `versions`
--

CREATE TABLE `versions` (
  `id` int(11) NOT NULL,
  `update_date` datetime NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `syllabi_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `contents_and_strategies`
--
ALTER TABLE `contents_and_strategies`
  ADD PRIMARY KEY (`id`),
  ADD KEY `syllabi_id` (`syllabi_id`);

--
-- Indices de la tabla `evaluations`
--
ALTER TABLE `evaluations`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `faculties`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `faculties_subjects`
  ADD PRIMARY KEY (`id`),
  ADD KEY `faculties_id` (`faculties_id`),
  ADD KEY `subjects_id` (`subjects_id`);

ALTER TABLE `subjects`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `syllabi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `evaluations_id` (`evaluations_id`),
  ADD KEY `subject_id` (`subject_id`),
  ADD KEY `faculty_id` (`faculty_id`);

ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `faculty_id` (`faculty_id`);

ALTER TABLE `users_subjects`
  ADD PRIMARY KEY (`id`),
  ADD KEY `users_id` (`users_id`),
  ADD KEY `subjects_id` (`subjects_id`);

ALTER TABLE `users_syllabi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `syllabi_id` (`syllabi_id`);

ALTER TABLE `versions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `syllabi_id` (`syllabi_id`);

ALTER TABLE `contents_and_strategies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

ALTER TABLE `evaluations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

ALTER TABLE `faculties`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

ALTER TABLE `faculties_subjects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

ALTER TABLE `subjects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

ALTER TABLE `syllabi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

ALTER TABLE `users_subjects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

ALTER TABLE `users_syllabi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `versions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `contents_and_strategies`
  ADD CONSTRAINT `contents_and_strategies_ibfk_1` FOREIGN KEY (`syllabi_id`) REFERENCES `syllabi` (`id`);

ALTER TABLE `faculties_subjects`
  ADD CONSTRAINT `faculties_subjects_ibfk_1` FOREIGN KEY (`faculties_id`) REFERENCES `faculties` (`id`),
  ADD CONSTRAINT `faculties_subjects_ibfk_2` FOREIGN KEY (`subjects_id`) REFERENCES `subjects` (`id`);

ALTER TABLE `syllabi`
  ADD CONSTRAINT `syllabi_ibfk_1` FOREIGN KEY (`evaluations_id`) REFERENCES `evaluations` (`id`),
  ADD CONSTRAINT `syllabi_ibfk_2` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`id`),
  ADD CONSTRAINT `syllabi_ibfk_3` FOREIGN KEY (`faculty_id`) REFERENCES `faculties` (`id`);

ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`faculty_id`) REFERENCES `faculties` (`id`);

ALTER TABLE `users_subjects`
  ADD CONSTRAINT `users_subjects_ibfk_1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `users_subjects_ibfk_2` FOREIGN KEY (`subjects_id`) REFERENCES `subjects` (`id`);

ALTER TABLE `users_syllabi`
  ADD CONSTRAINT `users_syllabi_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `users_syllabi_ibfk_2` FOREIGN KEY (`syllabi_id`) REFERENCES `syllabi` (`id`);

ALTER TABLE `versions`
  ADD CONSTRAINT `versions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `versions_ibfk_2` FOREIGN KEY (`syllabi_id`) REFERENCES `syllabi` (`id`);
COMMIT;
