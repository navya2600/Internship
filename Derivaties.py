from manim import *

class DerivativesIntro(Scene):
    def construct(self):
        # Title
        title = Text("Understanding Derivatives", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Definition
        definition = Tex("The derivative measures how a function changes.")
        definition.next_to(title, DOWN)
        self.play(Write(definition))
        self.wait(2)
        
        # Graphing function and secant line
        axes = Axes(x_range=[-3, 3], y_range=[-1, 9], axis_config={"include_numbers": True})
        function = axes.plot(lambda x: x**2, color=BLUE)
        function_label = MathTex("f(x) = x^2").next_to(function, UR, buff=0.5)
        
        point_a = Dot(axes.coords_to_point(1, 1), color=YELLOW)
        point_b = Dot(axes.coords_to_point(2, 4), color=YELLOW)
        secant_line = Line(point_a.get_center(), point_b.get_center(), color=RED)
        
        self.play(Create(axes))
        self.play(Create(function), Write(function_label))
        self.wait(1)
        self.play(FadeIn(point_a, point_b))
        self.play(Create(secant_line))
        self.wait(2)
        
        # Tangent line using TangentLine instead of deprecated function
        tangent_line = TangentLine(function, alpha=0.33, length=4, color=GREEN)
        self.play(Create(tangent_line))
        self.wait(2)
        
        # Power Rule Example
        power_rule = MathTex("\\frac{d}{dx} x^n = n x^{n-1}")
        power_rule.to_edge(DOWN)
        self.play(Write(power_rule))
        self.wait(2)
        
        example = MathTex("\\frac{d}{dx} x^2 = 2x")
        example.next_to(power_rule, UP)
        self.play(Write(example))
        self.wait(2)
        
        # Application: Velocity
        velocity_eq = MathTex("v = \\frac{ds}{dt}", color=ORANGE)
        velocity_eq.to_edge(DOWN)
        self.play(Write(velocity_eq))
        self.wait(2)
        
        self.play(FadeOut(title, definition, function_label, point_a, point_b, secant_line, tangent_line, power_rule, example, velocity_eq))
        
        # Closing statement
        closing_text = Text("Derivatives help us understand change!")
        self.play(Write(closing_text))
        self.wait(2)

if __name__ == "__main__":
    from manim import config
    config.media_width = "75%"
    scene = DerivativesIntro()
    scene.render()
