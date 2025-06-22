# Vocalization
Analysis of coupled nonlinear oscillators in mammalian vocalizations using van der Pol Oscillator (representing the vocal folds) and Duffing oscillator (representing the false vocal folds)

## Van der Pol
$\ddot{x} - \mu (1 - x^2) \dot{x} + x = 0$


$\mu$ : nonlinearity and damping parameter 
      (controls the strength of the nonlinear damping)

## Duffing

$\ddot{y} + \gamma \dot{y} + \alpha y + \beta y^3 = 0$

$\gamma$ : amplitude of the external driving force


$\alpha$ : linear stiffness coefficient


$\beta$ : nonlinear stiffness coefficient (controls the strength of the cubic term)

## Coupling Variations
Depending how to drive the Duffingoscillator, there are variation of:

ondirectional coupling ($\ddot{y} + \gamma \dot{y} + \alpha y + \beta y^3 = k x$)

bidirectional coupling ($\ddot{y} + \gamma \dot{y} + \alpha y + \beta y^3 = k x$ and $\ddot{x} - \mu (1 - x^2) \dot{x} + x = k y$) 

parametric coupling ($\ddot{y} + \gamma \dot{y} + \alpha y + \beta y^3 = k x y$)


k : coupling constant