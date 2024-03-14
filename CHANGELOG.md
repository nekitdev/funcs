# Changelog

<!-- changelogging: start -->

## 0.9.2 (2024-03-14)

### Internal

- `TypeIs` is now used instead of `TypeGuard` for more precise type narrowing.

## 0.9.1 (2024-02-26)

No significant changes.

## 0.9.0 (2024-02-24)

### Internal

- Dropped Python 3.7 support.

## 0.8.0 (2023-05-31)

### Features

- Added `awaiting` function.

## 0.7.1 (2023-05-24)

### Fixes

- Fixed `final` import to be compatible with Python 3.7.

## 0.7.0 (2023-05-22)

### Features

- Added `@cache` and `@cache_typed` decorators.

## 0.6.0 (2023-05-21)

### Removals

- Removed `funcs.typing` module. Consider using `typing-aliases` library instead.

## 0.5.1 (2023-04-24)

### Features

- Exported the `inspect` function (from `funcs.debug`).

## 0.5.0 (2023-04-23)

### Changes

- `Error`, `ErrorType` and `ErrorTypes` have been renamed to `NormalError`, `NormalErrorType`
  and `NormalErrorTypes` respectively.

## 0.4.0 (2023-04-21)

### Features

- Documented the entire library.

## 0.3.0 (2023-04-20)

### Features

- Added `asyncify` function.

## 0.2.4 (2023-04-18)

### Features

- Added `DynamicAsyncCallable` and `AnyAsyncCallable` types to `funcs.typing`.

## 0.2.3 (2023-04-18)

### Features

- Added `TupleN` (homogenous tuples) and `Compare` (comparing functions) to `funcs.typing`.

## 0.2.2 (2023-04-17)

### Features

- Added more types to `funcs.typing` module, for instance, `Identity`, `Inspect`, `Decorator`.

## 0.2.1 (2023-04-12)

### Features

- Added metadata to the library.

## 0.2.0 (2023-04-12)

Initial release.
