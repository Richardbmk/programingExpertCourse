// This suite of tests is written to run against your code
// so that we can check its correctness.

package main

import (
	"github.com/stretchr/testify/require"
)

func (s *TestSuite) TestCase1(t *TestCase) {
	expected := "violet"
	output := ColorMaker("red", "blue")
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase2(t *TestCase) {
	expected := "violet"
	output := ColorMaker("blue", "red")
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase3(t *TestCase) {
	expected := "orange"
	output := ColorMaker("yellow", "red")
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase4(t *TestCase) {
	expected := "orange"
	output := ColorMaker("red", "yellow")
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase5(t *TestCase) {
	expected := "green"
	output := ColorMaker("blue", "yellow")
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase6(t *TestCase) {
	expected := "green"
	output := ColorMaker("yellow", "blue")
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase7(t *TestCase) {
	expected := "red"
	output := ColorMaker("red", "red")
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase8(t *TestCase) {
	expected := "blue"
	output := ColorMaker("blue", "blue")
	require.Equal(t, expected, output)
}

func (s *TestSuite) TestCase9(t *TestCase) {
	expected := "yellow"
	output := ColorMaker("yellow", "yellow")
	require.Equal(t, expected, output)
}
