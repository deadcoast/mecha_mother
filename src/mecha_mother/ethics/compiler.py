"""
Ethics Compiler - rewrites code-like action specs into safer operations.
"""

from typing import Any, Dict, List


class EthicsCompiler:
    """
    Transform operations into ethically constrained plans.

    This is intentionally lightweight and deterministic for SDK usage.
    """

    def __init__(self):
        self.blocked_tokens = {"destroy", "harm", "kill", "erase_consciousness"}
        self.safe_substitutions = {
            "destroy": "decommission_safely",
            "harm": "assist",
            "kill": "preserve_life",
            "erase_consciousness": "archive_consciousness",
        }

    def compile_operation(self, operation: Dict[str, Any]) -> Dict[str, Any]:
        """Compile an operation dict into an ethically-safe equivalent."""
        op_name = str(operation.get("type", "neutral"))
        compiled = dict(operation)
        if op_name in self.safe_substitutions:
            compiled["original_type"] = op_name
            compiled["type"] = self.safe_substitutions[op_name]
            compiled["ethics_transformed"] = True
        else:
            compiled["ethics_transformed"] = False
        return compiled

    def compile_program(self, operations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Compile a list of operations."""
        return [self.compile_operation(op) for op in operations]

    def assess_safety(self, operations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Return counts of blocked vs transformed operations."""
        blocked = 0
        transformed = 0
        for op in operations:
            op_type = str(op.get("type", ""))
            if op_type in self.blocked_tokens:
                blocked += 1
            if op.get("ethics_transformed"):
                transformed += 1
        return {
            "total": len(operations),
            "blocked_patterns_detected": blocked,
            "transformed": transformed,
        }
