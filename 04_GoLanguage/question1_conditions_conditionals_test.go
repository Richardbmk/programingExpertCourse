// This suite of tests is written to run against your code
// so that we can check its correctness.

package main

import (
	"github.com/stretchr/testify/require"
)

func (s *TestSuite) TestCase1(t *TestCase) {
	expected := true
	output := VerifyLogin("ProgrammingExpert", "LearnToCode", 4)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase2(t *TestCase) {
	expected := false
	output := VerifyLogin("ProgrammingExpert", "Code", 4)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase3(t *TestCase) {
	expected := false
	output := VerifyLogin("ProgrammingExpert", "LearnToCode", 7)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase4(t *TestCase) {
	expected := false
	output := VerifyLogin("", "LearnToCode", 3)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase5(t *TestCase) {
	expected := true
	output := VerifyLogin("ProgrammingExpert", "LearnToCode", 1)
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase6(t *TestCase) {
	expected := false
	output := VerifyLogin("Programming", "LearnToExpert", -1)
	require.Equal(t, expected, output)
}
