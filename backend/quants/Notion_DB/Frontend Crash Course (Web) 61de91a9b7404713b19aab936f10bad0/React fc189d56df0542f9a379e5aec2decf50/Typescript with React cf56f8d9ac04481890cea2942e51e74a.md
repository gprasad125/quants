# Typescript with React

> Simpler than you think
> 

---

# Intro

This doc just gives examples of some things you will have to do when using Typescript with React. 

Definitely check out [Ben Awad’s walkthrough](https://www.youtube.com/watch?v=Z5iWr6Srsj8&ab_channel=BenAwad) if you have the time as well. It’s rather old (don’t use `React.FC`) but it covers most of what you’ll need.

Most of the types should be automatically inferred by Typescript, so you likely won’t need to change much. But occasionally, like with props, you’ll have to do some explicit typing to help yourself later. 

# Typing component props

```tsx
type Props = { // you can use an interface here as well
	count: number,
	text: string,
	class?: string
};

function SomeComponent({ count, text, class }: Props) {
	// ...
	return ( 
		// pass class property to children
		<div className={(class ? class : '')}>
			{/* ... */}
		</div> 
	);
}

// properties will have type checking
<SomeComponent 
	count={5}
	text='hello'
	class='mb-5'
/>
```

# Typing states and references

```tsx
// if you want it to be undefined at first, but enforce type later
const { count, setCount } = useState<number>();

// if you want it to be nullable
const { count, setCount } = useState<number | null>(null);

// typescript can infer automatically if you give default
const { count, setCount } = useState(5);

// otherwise can explicitly specify
const { count, setCount } = useState<number>(5);

// same for nested data
const { countArray, setCountArray } = useState<number[]>([]);

// everything same for useRef
const countRef = useRef<number>();
```