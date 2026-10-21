# -*- coding: utf-8 -*-
"""Carrier DIM Weight Packaging Optimizer for GenPark Agentic Commerce."""
import json
import math
from typing import Dict, Any

class CarrierDIMWeightPackagingOptimizer:
    @staticmethod
    def calculate_billable_shipping_weight(length_in: float, width_in: float, height_in: float, actual_weight_lbs: float, dim_divisor: int = 139) -> Dict[str, Any]:
        cubic_inches = length_in * width_in * height_in
        dim_weight = math.ceil(cubic_inches / dim_divisor)
        billable = max(math.ceil(actual_weight_lbs), dim_weight)
        is_dim_penalized = dim_weight > actual_weight_lbs
        return {"actual_lbs": actual_weight_lbs, "dim_lbs": dim_weight, "billable_weight_lbs": billable, "is_shipping_air": is_dim_penalized, "excess_billed_lbs": max(0, billable - math.ceil(actual_weight_lbs))}

    @staticmethod
    def optimize_box_size_to_reduce_air(current_billable_lbs: float, product_volume_cu_in: float) -> Dict[str, Any]:
        target_dim_lbs = math.ceil(product_volume_cu_in * 1.20 / 139)
        savings_lbs = max(0, current_billable_lbs - target_dim_lbs)
        return {"current_billable_lbs": current_billable_lbs, "rightsized_billable_lbs": target_dim_lbs, "billable_weight_saved_lbs": savings_lbs, "estimated_freight_savings_usd": round(savings_lbs * 1.85, 2)}
