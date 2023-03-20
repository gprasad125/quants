import s from '../styles/footer.module.scss';
import Link from './link';

function Footer() {
	return (
		<div className={s.footer + ' py-5 w-full sm:fixed sm:bottom-0'}>
			<div className='container max-w-2xl mx-auto px-5'>
				<p className={'mb-3 ' + s['gray-muted']}>
					quads (query any data set) takes q&a to the next level. quads ai is not liable for content generated. do not enter personal information.
				</p>
				<hr className={'mb-3 ' + s['border-gray-dark']} />
				<div>
					<img 
						className='inline-block mr-5 h-8 w-8' 
						src="/quants_logo_black.png" 
						alt="quads logo" 
					/>
					<Link className='inline-block mr-5' href='#' text='privacy policy' />
					<Link className='inline-block mr-5' href='#' text='about' />
					<Link className='inline-block' href='#' text='contact us' />
				</div>
			</div>
		</div>
	);
}

export default Footer;
