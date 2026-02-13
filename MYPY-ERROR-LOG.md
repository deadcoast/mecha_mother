# mypy-error-output.md

> uv run mypy src --check-untyped-defs
```ps1
mecha_mother on  main [!+?] is 📦 v0.1.0 via 🐍 v3.11.14 (mecha_mother) 
❯ mypy src --check-untyped-defs
src\mecha_mother\ethics\decision.py:66: error: Incompatible types in assignment (expression has type "float", variable has type "floating[Any]")  [assignment]
src\mecha_mother\reality\reality.py:1285: error: Incompatible types in assignment (expression has type "RealityConfig", target has type "dict[str, ndarray[tuple[Any, ...], dtype[Any]] | None]")  [assignment]
src\mecha_mother\reality\reality.py:1286: error: Incompatible types in assignment (expression has type "str", target has type "dict[str, ndarray[tuple[Any, ...], dtype[Any]] | None]")  [assignment]
```

