import React, { useState, useEffect, useContext, useReducer, useRef, useMemo, useCallback, useLayoutEffect, useImperativeHandle, forwardRef } from 'react';

// useState Example
function Counter() {
    const [count, setCount] = useState(0);
    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={() => setCount(count + 1)}>Increment</button>
        </div>
    );
}

// useEffect Example
function Timer() {
    const [time, setTime] = useState(0);
    useEffect(() => {
        const interval = setInterval(() => setTime((t) => t + 1), 1000);
        return () => clearInterval(interval); // Cleanup
    }, []);
    return <p>Time: {time}s</p>;
}

// useContext Example
const ThemeContext = React.createContext('light');
function ThemedComponent() {
    const theme = useContext(ThemeContext);
    return <p>Current theme: {theme}</p>;
}

// useReducer Example
function CounterWithReducer() {
    const reducer = (state, action) => {
        switch (action.type) {
            case 'increment':
                return { count: state.count + 1 };
            case 'decrement':
                return { count: state.count - 1 };
            default:
                throw new Error();
        }
    };
    const [state, dispatch] = useReducer(reducer, { count: 0 });
    return (
        <div>
            <p>Count: {state.count}</p>
            <button onClick={() => dispatch({ type: 'increment' })}>+</button>
            <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
        </div>
    );
}

// useRef Example
function InputFocus() {
    const inputRef = useRef(null);
    return (
        <div>
            <input ref={inputRef} type="text" />
            <button onClick={() => inputRef.current.focus()}>Focus Input</button>
        </div>
    );
}

// useMemo Example
function ExpensiveCalculation({ num }) {
    const calculate = (n) => {
        console.log('Calculating...');
        return n * 2;
    };
    const result = useMemo(() => calculate(num), [num]);
    return <p>Result: {result}</p>;
}

// useCallback Example
function CallbackExample({ onClick }) {
    const handleClick = useCallback(() => {
        console.log('Button clicked');
        onClick();
    }, [onClick]);
    return <button onClick={handleClick}>Click Me</button>;
}

// useLayoutEffect Example
function LayoutEffectExample() {
    const divRef = useRef(null);
    useLayoutEffect(() => {
        console.log('Div width:', divRef.current.offsetWidth);
    }, []);
    return <div ref={divRef} style={{ width: '100px', height: '100px', background: 'lightblue' }} />;
}

// useImperativeHandle Example
const CustomInput = forwardRef((props, ref) => {
    const inputRef = useRef();
    useImperativeHandle(ref, () => ({
        focus: () => inputRef.current.focus(),
    }));
    return <input ref={inputRef} type="text" />;
});
function ImperativeHandleExample() {
    const inputRef = useRef();
    return (
        <div>
            <CustomInput ref={inputRef} />
            <button onClick={() => inputRef.current.focus()}>Focus Input</button>
        </div>
    );
}

export default function App() {
    return (
        <div>
            <h1>React Hooks Examples</h1>
            <Counter />
            <Timer />
            <ThemeContext.Provider value="dark">
                <ThemedComponent />
            </ThemeContext.Provider>
            <CounterWithReducer />
            <InputFocus />
            <ExpensiveCalculation num={5} />
            <CallbackExample onClick={() => alert('Clicked!')} />
            <LayoutEffectExample />
            <ImperativeHandleExample />
        </div>
    );
}
