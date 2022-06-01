cmake_minimum_required(VERSION 3.22)
project(leetcode)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(leetcode
        0001.Two_sum.cpp
        0002.AddTwoNumbers.cpp
        0003.LongestSubstringWithoutRepeatingCharacters.cpp
        0009.PalindromeNumber.cpp
        0013.Roman_to_Integer.cpp
        0014.LongestCommonPrefix.cpp
        0020.ValidParentheses.cpp
        0021.MergeTwoSortedLists.cpp
        0118.pascals_triangle.cpp
        "0119.Pascal's_Triangle II.cpp"
        2011.FinalValueofVariableAfterPerformingOperations.cpp
        leetcode.h 0026.RemoveDuplicatesFromSortedArray.cpp 0027.RemoveElement.cpp "0028.Implement_strStr().cpp" 0035.Search_Insert_position.cpp 0278.First_bad_version.cpp 0053.Maximum_subarry.cpp 0697.Degree_of_an_array.cpp 0645.Set_Mismatch.cpp)
