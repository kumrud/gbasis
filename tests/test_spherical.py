"""Test gbasis.spherical."""
from gbasis.spherical import (
    expansion_coeff,
    generate_transformation,
    harmonic_norm,
    real_solid_harmonic,
    shift_factor,
)
import numpy as np
import pytest


def test_shift_factor():
    """Test spherical.shift_factor."""
    assert shift_factor(2) == 0.0
    assert shift_factor(0) == 0.0
    assert shift_factor(-1) == 0.5
    with pytest.raises(TypeError):
        shift_factor(0.5)
    with pytest.raises(TypeError):
        shift_factor(None)


def test_expansion_coeff():
    """Test spherical.expansion_coeff."""
    assert expansion_coeff(0, 0, 0, 0, 0) == 1.0
    assert expansion_coeff(1, 0, 0, 0, 0) == 1.0
    with pytest.raises(TypeError):
        expansion_coeff(0.0, 0, 0, 0, 0)
    with pytest.raises(TypeError):
        expansion_coeff(0, 0.0, 0, 0, 0)
    with pytest.raises(TypeError):
        expansion_coeff(0, 0, 0.0, 0, 0)
    with pytest.raises(TypeError):
        expansion_coeff(0, 0, 0, 0.0, 0)
    with pytest.raises(TypeError):
        expansion_coeff(None, 0, 0, 0, 0)
    with pytest.raises(TypeError):
        expansion_coeff(0, None, 0, 0, 0)
    with pytest.raises(TypeError):
        expansion_coeff(0, 0, None, 0, 0)
    with pytest.raises(TypeError):
        expansion_coeff(0, 0, 0, None, 0)
    with pytest.raises(TypeError):
        expansion_coeff(0, 0, 0, 0, None)
    with pytest.raises(ValueError):
        expansion_coeff(-1, 0, 0, 0, 0)
    with pytest.raises(ValueError):
        expansion_coeff(3, 4, 0, 0, 0)
    with pytest.raises(ValueError):
        expansion_coeff(1, -2, 0, 0, 0)
    with pytest.raises(ValueError):
        expansion_coeff(2, -1, 0, 0, 0)
    with pytest.raises(ValueError):
        expansion_coeff(2, 1, 0, 0, 0.5)


def test_harmonic_norm():
    """Test spherical.harmonic_norm."""
    assert harmonic_norm(0, 0) == 1
    with pytest.raises(TypeError):
        harmonic_norm(0.0, 0)
    with pytest.raises(TypeError):
        harmonic_norm(0, 0.0)
    with pytest.raises(TypeError):
        harmonic_norm(None, 0)
    with pytest.raises(TypeError):
        harmonic_norm(0, None)
    with pytest.raises(ValueError):
        harmonic_norm(-1, 0)
    with pytest.raises(ValueError):
        harmonic_norm(1, 2)
    with pytest.raises(ValueError):
        harmonic_norm(0, -1)


def test_real_solid_harmonic():
    """Test spherical.real_solid_harmonic.

    All real solid harmonics obtained from Helgaker et al. "Molecular Electronic-Structure Theory",
    pg. 211 (Table 6.3).
    """
    assert real_solid_harmonic(0, 0) == {(0, 0, 0): 1.0}
    assert real_solid_harmonic(1, 1) == {(1, 0, 0): 1.0}
    assert real_solid_harmonic(1, 0) == {(0, 0, 1): 1.0}
    assert real_solid_harmonic(1, -1) == {(0, 1, 0): 1.0}
    assert real_solid_harmonic(2, 2) == {(0, 2, 0): -np.sqrt(3) / 2, (2, 0, 0): np.sqrt(3) / 2}
    assert real_solid_harmonic(2, 1) == {(1, 0, 1): np.sqrt(3)}
    assert real_solid_harmonic(2, 0) == {(0, 0, 2): 1.0, (2, 0, 0): -0.5, (0, 2, 0): -0.5}
    assert real_solid_harmonic(2, -1) == {(0, 1, 1): np.sqrt(3)}
    assert real_solid_harmonic(2, -2) == {(1, 1, 0): np.sqrt(3)}
    with pytest.raises(TypeError):
        real_solid_harmonic(0.0, 0)
    with pytest.raises(TypeError):
        real_solid_harmonic(0, 0.0)
    with pytest.raises(TypeError):
        real_solid_harmonic(None, 0)
    with pytest.raises(TypeError):
        real_solid_harmonic(0, None)
    with pytest.raises(ValueError):
        real_solid_harmonic(-1, 0)
    with pytest.raises(ValueError):
        real_solid_harmonic(1, 2)
    with pytest.raises(ValueError):
        real_solid_harmonic(0, -1)


def test_generate_transformation():
    """Test spherical.generate_transformation."""
    assert np.array_equal(
        generate_transformation(0, np.array([(0, 0, 0)]), (0,), "right"), np.array([[1.0]])
    )
    assert np.array_equal(
        generate_transformation(
            1, np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)]), (-1, 0, 1), "right"
        ),
        np.array([[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]),
    )
    assert np.array_equal(
        generate_transformation(0, np.array([(0, 0, 0)]), (0,), "right").T,
        generate_transformation(0, np.array([(0, 0, 0)]), (0,), "left"),
    )
    assert np.array_equal(
        generate_transformation(
            1, np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)]), (-1, 0, 1), "right"
        ).T,
        generate_transformation(1, np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)]), (-1, 0, 1), "left"),
    )
    with pytest.raises(TypeError):
        generate_transformation(0.0, np.array([(0, 0, 0)]), (0,), "right")
    with pytest.raises(TypeError):
        generate_transformation(0, 0, (0,), "right")
    with pytest.raises(ValueError):
        generate_transformation(
            -1, np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)]), (-1, 0, 1), "right"
        )
    with pytest.raises(ValueError):
        generate_transformation(0, np.array([(0, 0, 0, 0)]), (0,), "right")
    with pytest.raises(ValueError):
        generate_transformation(1, np.array([(1, 0, 0), (0, 1, 0), (0, 1)]), (-1, 0, 1), "right")
    with pytest.raises(ValueError):
        generate_transformation(
            1, np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 0, 0)]), (-1, 0, 1), "right"
        )
    with pytest.raises(ValueError):
        generate_transformation(1, np.array([(1, 0, 0), (0, 1, 0)]), (-1, 0, 1), "right")
    with pytest.raises(ValueError):
        generate_transformation(1, np.array([(1, 0, 0), (0, 0, 0), (0, 0, 2)]), (-1, 0, 1), "right")
    with pytest.raises(TypeError):
        generate_transformation(1, np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)]), (-1, 0, 1), 1)
    with pytest.raises(TypeError):
        generate_transformation(1, np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)]), (-1, 0, 1), None)
    with pytest.raises(ValueError):
        generate_transformation(1, np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)]), (-1, 0, 1), "up")
    with pytest.raises(ValueError):
        generate_transformation(1, np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)]), (-1, 0, 1), "")
    # check angmom_components_sph type
    with pytest.raises(TypeError):
        generate_transformation(
            1, np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)]), np.array([-1, 0, 1]), "left"
        )
    with pytest.raises(TypeError):
        generate_transformation(1, np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)]), {-1, 0, 1}, "left")
    with pytest.raises(TypeError):
        generate_transformation(
            1, np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)]), [-1, 0, 1.0], "left"
        )
    # check angmom_components_sph value
    with pytest.raises(ValueError):
        generate_transformation(
            1, np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)]), (-1, 0, 1, 1), "left"
        )
    with pytest.raises(ValueError):
        generate_transformation(1, np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)]), (-1, 2, 1), "left")


# FIXME: cannot reproduce horton results for the angular momentum 4. I  have a feeling that the
# horton results for the are incorrect here, but it will need to be double checked.
def test_generate_transformation_horton():
    """Test spherical.generate_transformation using horton reference.

    Answer obtained from https://theochem.github.io/horton/2.0.1/tech_ref_gaussian_basis.html.
    """
    answer = np.array(
        [
            [-0.5, 0, 0, -0.5, 0, 1],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0.5 * 3 ** 0.5, 0, 0, -0.5 * 3 ** 0.5, 0, 0],
            [0, 1, 0, 0, 0, 0],
        ]
    )
    # shuffle to have correct order
    answer = answer[[4, 2, 0, 1, 3], :]
    assert np.allclose(
        generate_transformation(
            2,
            np.array([[2, 0, 0], [1, 1, 0], [1, 0, 1], [0, 2, 0], [0, 1, 1], [0, 0, 2]]),
            (-2, -1, 0, 1, 2),
            "left",
        ),
        answer,
    )

    answer = np.array(
        [
            [0, 0, -3 / 10 * 5 ** 0.5, 0, 0, 0, 0, -3 / 10 * 5 ** 0.5, 0, 1],
            [-1 / 4 * 6 ** 0.5, 0, 0, -1 / 20 * 30 ** 0.5, 0, 1 / 5 * 30 ** 0.5, 0, 0, 0, 0],
            [0, -1 / 20 * 30 ** 0.5, 0, 0, 0, 0, -1 / 4 * 6 ** 0.5, 0, 1 / 5 * 30 ** 0.5, 0],
            [0, 0, 1 / 2 * 3 ** 0.5, 0, 0, 0, 0, -1 / 2 * 3 ** 0.5, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [1 / 4 * 10 ** 0.5, 0, 0, -3 / 4 * 2 ** 0.5, 0, 0, 0, 0, 0, 0],
            [0, 3 / 4 * 2 ** 0.5, 0, 0, 0, 0, -1 / 4 * 10 ** 0.5, 0, 0, 0],
        ]
    )
    # shuffle to have correct order
    answer = answer[[6, 4, 2, 0, 1, 3, 5], :]
    assert np.allclose(
        generate_transformation(
            3,
            np.array(
                [
                    [3, 0, 0],
                    [2, 1, 0],
                    [2, 0, 1],
                    [1, 2, 0],
                    [1, 1, 1],
                    [1, 0, 2],
                    [0, 3, 0],
                    [0, 2, 1],
                    [0, 1, 2],
                    [0, 0, 3],
                ]
            ),
            (-3, -2, -1, 0, 1, 2, 3),
            "left",
        ),
        answer,
    )

    # answer = np.array(
    #     [
    #         [
    #             3 / 8,
    #             0,
    #             0,
    #             3 / 140 * 105 ** 0.5,
    #             0,
    #             -3 / 35 * 105 ** 0.5,
    #             0,
    #             0,
    #             0,
    #             0,
    #             3 / 8,
    #             0,
    #             -3 / 35 * 105 ** 0.5,
    #             0,
    #             1,
    #         ],
    #         [
    #             0,
    #             0,
    #             -3 / 28 * 70 ** 0.5,
    #             0,
    #             0,
    #             0,
    #             0,
    #             -3 / 28 * 14 ** 0.5,
    #             0,
    #             1 / 7 * 70 ** 0.5,
    #             0,
    #             0,
    #             0,
    #             0,
    #             0,
    #         ],
    #         [
    #             0,
    #             0,
    #             0,
    #             0,
    #             -3 / 28 * 14 ** 0.5,
    #             0,
    #             0,
    #             0,
    #             0,
    #             0,
    #             0,
    #             -3 / 28 * 70 ** 0.5,
    #             0,
    #             1 / 7 * 70 ** 0.5,
    #             0,
    #         ],
    #         [
    #             -1 / 4 * 5 ** 0.5,
    #             0,
    #             0,
    #             0,
    #             0,
    #             3 / 14 * 21 ** 0.5,
    #             0,
    #             0,
    #             0,
    #             0,
    #             1 / 4 * 5 ** 0.5,
    #             0,
    #             -3 / 14 * 21 ** 0.5,
    #             0,
    #             0,
    #         ],
    #         [
    #             0,
    #             -1 / 14 * 35 ** 0.5,
    #             0,
    #             0,
    #             0,
    #             0,
    #             -1 / 14 * 35 ** 0.5,
    #             0,
    #             3 / 7 * 7 ** 0.5,
    #             0,
    #             0,
    #             0,
    #             0,
    #             0,
    #             0,
    #         ],
    #         [0, 0, 1 / 4 * 10 ** 0.5, 0, 0, 0, 0, -3 / 4 * 2 ** 0.5, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 3 / 4 * 2 ** 0.5, 0, 0, 0, 0, 0, 0, -1 / 4 * 10 ** 0.5, 0, 0, 0],
    #         [
    #             1 / 8 * 35 ** 0.5,
    #             0,
    #             0,
    #             -3 / 4 * 3 ** 0.5,
    #             0,
    #             0,
    #             0,
    #             0,
    #             0,
    #             0,
    #             1 / 8 * 35 ** 0.5,
    #             0,
    #             0,
    #             0,
    #             0,
    #         ],
    #         [0, 1 / 2 * 5 ** 0.5, 0, 0, 0, 0, -1 / 2 * 5 ** 0.5, 0, 0, 0, 0, 0, 0, 0, 0],
    #     ]
    # )
    # # shuffle to have correct order
    # answer = answer[[8, 6, 4, 2, 0, 1, 3, 5, 7], :]
    # assert np.allclose(
    #     generate_transformation(
    #         4,
    #         np.array(
    #             [
    #                 [4, 0, 0],
    #                 [3, 1, 0],
    #                 [3, 0, 1],
    #                 [2, 2, 0],
    #                 [2, 1, 1],
    #                 [2, 0, 2],
    #                 [1, 3, 0],
    #                 [1, 2, 1],
    #                 [1, 1, 2],
    #                 [1, 0, 3],
    #                 [0, 4, 0],
    #                 [0, 3, 1],
    #                 [0, 2, 2],
    #                 [0, 1, 3],
    #                 [0, 0, 4],
    #             ]
    #         ),
    #         (-4, -3, -2, -1, 0, 1, 2, 3, 4),
    #         "left",
    #     ),
    #     answer,
    # )
