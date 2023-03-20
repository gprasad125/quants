import s from '../styles/navbar.module.scss';
import Link from './link';

function Navbar() {
	return (
		<div className={'px-8 sm:px-20 flex flex-row justify-between flex-nowrap items-center ' + s.nav}>
			<img className='grow-0' src="/quants_logo_black.png" alt="quads logo" />
			<nav className='py-5'>
				<Link href='#' text='about' className='mr-10' />
				<Link href='#' text='contact us' />
			</nav>
		</div>
	);
}

export default Navbar;
