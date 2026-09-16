def average(nums: list[int]) -> float:
    """
    Gives the average value of given of numbers.

    Args:
        nums:(list[int]): List of numbers

    Returns:
        float: average value of given list of numbers

    """

    return sum(nums) / len(nums)

def median(nums: list[int]) -> float:
    """
    Gives the Median value of given of numbers.

    Args:
        nums:(list[int]): List of numbers

    Returns:
        float: Median value of given list of numbers

    """

    return sorted(nums) [ len(nums) // 2]

def mode(nums: list[int]) -> float:
    """
    Gives the mode value of given of numbers.

    Args:
        nums:(list[int]): List of numbers

    Returns:
        float: mode value of given list of numbers

    """

    return max(set(nums), key=nums.count)
